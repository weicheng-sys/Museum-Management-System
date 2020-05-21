"use strict";

exports.__esModule = true;
exports.pickerProps = void 0;
var pickerProps = {
  title: String,
  loading: Boolean,
  showToolbar: Boolean,
  cancelButtonText: String,
  confirmButtonText: String,
  allowHtml: {
    type: Boolean,
    default: true
  },
  visibleItemCount: {
    type: [Number, String],
    default: 5
  },
  itemHeight: {
    type: [Number, String],
    default: 44
  },
  swipeDuration: {
    type: [Number, String],
    default: 1000
  }
};
exports.pickerProps = pickerProps;