'use strict';

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _enzyme = require('enzyme');

var _Tabs = require('../Tabs');

var _Tab = require('../Tab');

var _TabContent = require('../TabContent');

var _theme = require('../theme.css');

var _theme2 = _interopRequireDefault(_theme);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

describe('Tabs', function () {
  var Composition = function (_Component) {
    _inherits(Composition, _Component);

    function Composition() {
      _classCallCheck(this, Composition);

      var _this = _possibleConstructorReturn(this, (Composition.__proto__ || Object.getPrototypeOf(Composition)).call(this));

      _this.state = { index: 0 };
      return _this;
    }

    _createClass(Composition, [{
      key: 'render',
      value: function render() {
        return _react2.default.createElement(
          _Tabs.Tabs,
          _extends({ index: this.state.index }, this.props),
          _react2.default.createElement(
            _Tab.Tab,
            { label: 'tab1' },
            'tab1'
          ),
          _react2.default.createElement(
            _Tab.Tab,
            { label: 'tab2' },
            'tab2'
          )
        );
      }
    }]);

    return Composition;
  }(_react.Component);

  it('defaults to only rendering the current tab', function () {
    var wrapper = (0, _enzyme.mount)(_react2.default.createElement(Composition, null));
    expect(wrapper.find(_TabContent.TabContent).length).toEqual(1);
    expect(wrapper.find(_TabContent.TabContent).first().prop('tabIndex')).toEqual(0);

    wrapper.instance().setState({ index: 1 });
    expect(wrapper.find(_TabContent.TabContent).length).toEqual(1);
    expect(wrapper.find(_TabContent.TabContent).first().prop('tabIndex')).toEqual(1);
  });

  it('renders inactive tabs when hideMode is set to display', function () {
    var wrapper = (0, _enzyme.mount)(_react2.default.createElement(Composition, { hideMode: 'display' }));
    expect(wrapper.find(_TabContent.TabContent).length).toEqual(2);
    expect(wrapper.find(_TabContent.TabContent).at(0).prop('hidden')).toEqual(false);
    expect(wrapper.find(_TabContent.TabContent).at(1).prop('hidden')).toEqual(true);

    wrapper.instance().setState({ index: 1 });
    expect(wrapper.find(_TabContent.TabContent).length).toEqual(2);
    expect(wrapper.find(_TabContent.TabContent).at(0).prop('hidden')).toEqual(true);
    expect(wrapper.find(_TabContent.TabContent).at(1).prop('hidden')).toEqual(false);
  });

  describe('#render', function () {
    it('does not use fixed by default', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Tabs.Tabs, { theme: _theme2.default }));
      expect(wrapper.find('div').first().prop('className')).not.toContain(_theme2.default.fixed);
    });

    it('uses fixed when set', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Tabs.Tabs, { fixed: true, theme: _theme2.default }));
      expect(wrapper.find('div').first().prop('className')).toContain(_theme2.default.fixed);
    });

    it('does not use inverse by default', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Tabs.Tabs, { theme: _theme2.default }));
      expect(wrapper.find('div').first().prop('className')).not.toContain(_theme2.default.inverse);
    });

    it('uses inverse when set', function () {
      var wrapper = (0, _enzyme.mount)(_react2.default.createElement(_Tabs.Tabs, { inverse: true, theme: _theme2.default }));
      expect(wrapper.find('div').first().prop('className')).toContain(_theme2.default.inverse);
    });
  });
});