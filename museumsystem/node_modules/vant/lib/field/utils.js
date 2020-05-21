"use strict";

exports.__esModule = true;
exports.formatNumber = formatNumber;

function formatNumber(value, allowDot) {
  if (allowDot) {
    var dotIndex = value.indexOf('.');

    if (dotIndex > -1) {
      value = value.slice(0, dotIndex + 1) + value.slice(dotIndex).replace(/\./g, '');
    }
  } else {
    value = value.split('.')[0];
  }

  var regExp = allowDot ? /[^0-9.]/g : /\D/g;
  return value.replace(regExp, '');
}