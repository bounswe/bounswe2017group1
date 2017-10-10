'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.Avatar = exports.avatarFactory = undefined;

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _reactCssThemr = require('react-css-themr');

var _identifiers = require('../identifiers');

var _FontIcon = require('../font_icon/FontIcon');

var _FontIcon2 = _interopRequireDefault(_FontIcon);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

var factory = function factory(FontIcon) {
  var Avatar = function Avatar(_ref) {
    var alt = _ref.alt,
        children = _ref.children,
        className = _ref.className,
        cover = _ref.cover,
        icon = _ref.icon,
        image = _ref.image,
        theme = _ref.theme,
        title = _ref.title,
        other = _objectWithoutProperties(_ref, ['alt', 'children', 'className', 'cover', 'icon', 'image', 'theme', 'title']);

    return _react2.default.createElement(
      'div',
      _extends({ 'data-react-toolbox': 'avatar', className: (0, _classnames2.default)(theme.avatar, className) }, other),
      children,
      cover && typeof image === 'string' && _react2.default.createElement('span', { 'aria-label': alt, className: theme.image, style: { backgroundImage: 'url(' + image + ')' } }),
      !cover && (typeof image === 'string' ? _react2.default.createElement('img', { alt: alt, className: theme.image, src: image }) : image),
      typeof icon === 'string' ? _react2.default.createElement(FontIcon, { className: theme.letter, value: icon, alt: alt }) : icon,
      title ? _react2.default.createElement(
        'span',
        { className: theme.letter },
        title[0]
      ) : null
    );
  };

  Avatar.propTypes = {
    alt: _react.PropTypes.string,
    children: _react.PropTypes.node,
    className: _react.PropTypes.string,
    cover: _react.PropTypes.bool,
    icon: _react.PropTypes.oneOfType([_react.PropTypes.string, _react.PropTypes.element]),
    image: _react.PropTypes.oneOfType([_react.PropTypes.string, _react.PropTypes.element]),
    theme: _react.PropTypes.shape({
      avatar: _react.PropTypes.string,
      image: _react.PropTypes.string,
      letter: _react.PropTypes.string
    }),
    title: _react.PropTypes.string
  };

  Avatar.defaultProps = {
    alt: '',
    cover: false
  };

  return Avatar;
};

var Avatar = factory(_FontIcon2.default);
exports.default = (0, _reactCssThemr.themr)(_identifiers.AVATAR)(Avatar);
exports.avatarFactory = factory;
exports.Avatar = Avatar;