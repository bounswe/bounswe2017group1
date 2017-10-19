'use strict';

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _enzyme = require('enzyme');

var _Input = require('../../input/Input');

var _ProgressBar = require('../../progress_bar/ProgressBar');

var _Slider = require('../Slider');

var _theme = require('../theme.css');

var _theme2 = _interopRequireDefault(_theme);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

describe('Slider', function () {
  describe('#positionToValue', function () {
    it('returns min when position is less than origin', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500 })).instance();
      instance.setState({ sliderStart: 500, sliderLength: 100 });
      expect(instance.positionToValue({ x: 400 })).toEqual(-500);
    });

    it('returns max when position is more and origin plus length', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500 })).instance();
      instance.setState({ sliderStart: 500, sliderLength: 100 });
      expect(instance.positionToValue({ x: 900 })).toEqual(500);
    });

    it('returns the proper position when the position is inside slider', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500 })).instance();
      instance.setState({ sliderStart: 500, sliderLength: 100 });
      expect(instance.positionToValue({ x: 520 })).toEqual(-300);
    });
  });

  describe('#trimValue', function () {
    it('rounds to the proper number', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: 0, max: 100, step: 0.1 })).instance();
      expect(instance.trimValue(57.16)).toEqual(57.2);
      expect(instance.trimValue(57.12)).toEqual(57.10);
    });

    it('returns min if number is less than min', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: 0, max: 100, step: 0.1 })).instance();
      expect(instance.trimValue(-57.16)).toEqual(0);
    });

    it('returns max if number is more than max', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: 0, max: 100, step: 0.1 })).instance();
      expect(instance.trimValue(257.16)).toEqual(100);
    });
  });

  describe('#valueForInput', function () {
    it('returns a fixed number when an integer is given', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: 0, max: 100, step: 0.01 })).instance();
      expect(instance.valueForInput(4)).toEqual('4.00');
    });

    it('returns a fixed number when a float is given', function () {
      var instance = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: 0, max: 100, step: 0.01 })).instance();
      expect(instance.valueForInput(4.06)).toEqual('4.06');
    });
  });

  describe('#knobOffset', function () {
    it('returns percentage offset of knob for slider with given min/max/value props', function () {
      var slider = (0, _enzyme.shallow)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500, value: -250 })).instance();
      expect(slider.knobOffset()).toEqual(25);
    });
  });

  describe('#render', function () {
    it('contains a linear progress bar with proper properties', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { min: 100, max: 1000, value: 140 }));
      var progress = wrapper.find(_ProgressBar.ProgressBar);
      expect(progress.props().mode).toEqual('determinate');
      expect(progress.props().type).toEqual('linear');
      expect(progress.props().value).toEqual(140);
      expect(progress.props().min).toEqual(100);
      expect(progress.props().max).toEqual(1000);
    });

    it('contains an input component if its editable', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { editable: true, value: 130 }));
      var slider = wrapper.instance();
      var input = wrapper.find(_Input.Input);
      expect(parseInt(input.props().value, 10)).toEqual(slider.props.value);
    });

    it('contains the proper number of snaps when snapped', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { editable: true, pinned: true, theme: _theme2.default }));
      var sliderNode = wrapper.find('div').first();
      expect(sliderNode.props().className).toContain(_theme2.default.ring);
      expect(sliderNode.props().className).toContain(_theme2.default.pinned);
    });
  });

  describe('#events', function () {
    it('sets pressed state when knob is clicked', function () {
      var onChange = jest.fn();
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500, onChange: onChange }));
      var knob = wrapper.childAt(0).childAt(0);
      knob.simulate('mouseDown');
      expect(wrapper.state().pressed).toEqual(true);
    });

    it('sets pressed state when knob is touched', function () {
      var onChange = jest.fn();
      var event = { touches: [{ pageX: 200 }] };
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500, onChange: onChange }));
      var knob = wrapper.childAt(0).childAt(0);
      knob.simulate('touchStart', event);
      expect(wrapper.state().pressed).toEqual(true);
    });

    it('sets a proper value when the slider is clicked', function () {
      var onChange = jest.fn();
      var event = { pageX: 200, pageY: 0 };
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500, onChange: onChange }));
      var instance = wrapper.instance();
      instance.setState({ sliderStart: 0, sliderLength: 1000 });
      instance.handleResize = function (evt, callback) {
        callback();
      };
      wrapper.childAt(0).simulate('mouseDown', event);
      expect(onChange).toHaveBeenCalledWith(-300);
    });

    it('sets a proper value when the slider is touched', function () {
      var onChange = jest.fn();
      var event = { touches: [{ pageX: 200, pageY: 0 }] };
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { min: -500, max: 500, onChange: onChange }));
      var instance = wrapper.instance();
      instance.setState({ sliderStart: 0, sliderLength: 1000 });
      instance.handleResize = function (evt, callback) {
        callback();
      };
      wrapper.childAt(0).simulate('touchStart', event);
      expect(onChange).toHaveBeenCalledWith(-300);
    });

    it('changes input value when slider changes', function () {
      var onChange = jest.fn();
      var event = { pageX: 900 };
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { editable: true, onChange: onChange }));
      var instance = wrapper.instance();
      instance.setState({ sliderStart: 0, sliderLength: 1000 });
      instance.handleResize = function (evt, callback) {
        callback();
      };
      wrapper.childAt(0).simulate('mouseDown', event);
      expect(onChange).toHaveBeenCalledWith(90);
    });

    it('changes its value when input is blurred', function () {
      var onChange = jest.fn();
      var event = { target: { value: '80' } };
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { editable: true, value: 50, onChange: onChange }));
      wrapper.find('input').simulate('change', event);
      wrapper.find('input').simulate('blur');
      expect(onChange).toHaveBeenCalled();
      expect(onChange.mock.calls[0][0]).toEqual(80);
    });

    it('calls onChange callback when the value is changed', function () {
      var onChange = jest.fn();
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Slider.Slider, { editable: true, value: 50, onChange: onChange }));
      wrapper.instance().setState({ sliderStart: 0, sliderLength: 1000 });
      wrapper.childAt(0).simulate('mouseDown', { pageX: 900, pageY: 0 });
      expect(onChange).toHaveBeenCalled();
    });
  });
});