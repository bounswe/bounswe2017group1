import React from 'react';
import ReactDOM from 'react-dom';

class Rector extends React.Component {

  constructor(props) {
		super(props);
		this.canvas = null;
		this.ctx = null;
		this.isDirty = false;
		this.isDrag = false;
		this.startX = -1;
		this.startY = -1;
		this.curX = -1;
		this.curY = -1;
		this.updateCanvas = this.updateCanvas.bind(this);
		this.addMouseEvents = this.addMouseEvents.bind(this);
		this.removeMouseEvents = this.removeMouseEvents.bind(this);
		this.onMouseDown = this.onMouseDown.bind(this);
		this.onMouseMove = this.onMouseMove.bind(this);
		this.onMouseUp = this.onMouseUp.bind(this);
  }
  
  componentDidMount(props) {
    this.ctx = this.canvas.getContext('2d')
    this.ctx.strokeStyle = this.props.strokeStyle
    this.ctx.lineWidth = this.props.lineWidth
		this.addMouseEvents()
  }

  updateCanvas(){
    if (this.isDrag) {
      requestAnimationFrame(this.updateCanvas)
    }
    if (! this.isDirty) {
      return
    }
    
    this.ctx.clearRect(0, 0, this.props.width, this.props.height)
    if (this.isDrag) {      
      const rect = {
        x: this.startX,
        y: this.startY,
        w: this.curX - this.startX,
        h: this.curY - this.startY,
      }
      this.ctx.strokeRect(rect.x, rect.y, rect.w, rect.h)  
    }  
    this.isDirty = false
  };

  componentWillUnmount() {
    this.removeMouseEvents()
  }

  addMouseEvents() {
    document.addEventListener('mousedown', this.onMouseDown, false);
    document.addEventListener('mousemove', this.onMouseMove, false);
    document.addEventListener('mouseup', this.onMouseUp, false);
  }
  removeMouseEvents() {
    document.removeEventListener('mousedown', this.onMouseDown, false);
    document.removeEventListener('mousemove', this.onMouseMove, false);
    document.removeEventListener('mouseup', this.onMouseUp, false);
  }

  onMouseDown(e){
		if(! (e.target.localName.toString() == "canvas")) return;
    this.isDrag = true
    this.curX = this.startX = e.offsetX
    this.curY = this.startY = e.offsetY
    requestAnimationFrame(this.updateCanvas)
  };

  onMouseMove(e){
		if(! (e.target.localName == "canvas")) return;
    if (! this.isDrag) return
    this.curX = e.offsetX
    this.curY = e.offsetY
    this.isDirty = true
  };
  
  onMouseUp(e){
		if(! (e.target.localName == "canvas")) return;
    this.isDrag = false
    this.isDirty = true
    
    const rect = {
      x: Math.min(this.startX, this.curX),
      y: Math.min(this.startY, this.curY),
      w: Math.abs(e.offsetX - this.startX),
      h: Math.abs(e.offsetY - this.startY),
		}
		
		this.props.onSelected(rect)
  };
  
  render() {
    return (
			<canvas
			className="annotation"
			style={this.props.style}
			width={this.props.width}
			height={this.props.height}
			ref={(c) => {this.canvas=c}}/>
		)
  }
}

Rector.defaultProps = {
	width: 320,
	height: 200,
	strokeStyle: '#F00',
	lineWidth: 1,
	onSelected: () => {},
};
	

export default Rector;