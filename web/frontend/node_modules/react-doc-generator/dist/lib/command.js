'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _commander = require('commander');

var _commander2 = _interopRequireDefault(_commander);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var pkg = require('../../package.json');

exports.default = function Command() {

    var list = function list(val) {
        val = val.replace(/[, ]+/g, ',').trim();
        return val.split(',').filter(function (value) {
            return value.length > 0;
        });
    };

    _commander2.default.version(pkg.version).usage('<dir> [options]').option('-x, --extensions <items>', 'Include only these file extensions. Default: js,jsx', list, ['js', 'jsx']).option('-i, --ignore <items>', 'Folders to ignore. Default: node_modules,__tests__,__mocks__', list, ['node_modules', '__tests__', '__mocks__']).option('-e, --exclude-patterns <items>', 'Filename patterns to exclude. Default: []', list, []).option('-t, --title [value]', 'Document title. Default: \'Components\'', 'Components').option('-o, --output <file>', 'Markdown file to write. Default: \'DOCUMENTATION.MD\'', 'DOCUMENTATION.MD').parse(process.argv);

    return _commander2.default;
}();