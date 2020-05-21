import { createNamespace } from '../utils';
import { stopPropagation } from '../utils/dom/event';
import { BORDER_TOP } from '../utils/constant';
import { BindEventMixin } from '../mixins/bind-event';
import Key from './Key';

var _createNamespace = createNamespace('number-keyboard'),
    createComponent = _createNamespace[0],
    bem = _createNamespace[1],
    t = _createNamespace[2];

var CLOSE_KEY_THEME = ['blue', 'big'];
var DELETE_KEY_THEME = ['delete', 'big', 'gray'];
export default createComponent({
  mixins: [BindEventMixin(function (bind) {
    if (this.hideOnClickOutside) {
      bind(document.body, 'touchstart', this.onBlur);
    }
  })],
  model: {
    event: 'update:value'
  },
  props: {
    show: Boolean,
    title: String,
    zIndex: [Number, String],
    closeButtonText: String,
    deleteButtonText: String,
    theme: {
      type: String,
      default: 'default'
    },
    value: {
      type: String,
      default: ''
    },
    extraKey: {
      type: String,
      default: ''
    },
    maxlength: {
      type: [Number, String],
      default: Number.MAX_VALUE
    },
    transition: {
      type: Boolean,
      default: true
    },
    showDeleteKey: {
      type: Boolean,
      default: true
    },
    hideOnClickOutside: {
      type: Boolean,
      default: true
    },
    safeAreaInsetBottom: {
      type: Boolean,
      default: true
    }
  },
  watch: {
    show: function show(val) {
      if (!this.transition) {
        this.$emit(val ? 'show' : 'hide');
      }
    }
  },
  computed: {
    keys: function keys() {
      var keys = [];

      for (var i = 1; i <= 9; i++) {
        keys.push({
          text: i
        });
      }

      switch (this.theme) {
        case 'default':
          keys.push({
            text: this.extraKey,
            theme: ['gray'],
            type: 'extra'
          }, {
            text: 0
          }, {
            theme: ['gray'],
            text: this.showDeleteKey ? this.deleteText : '',
            type: this.showDeleteKey ? 'delete' : ''
          });
          break;

        case 'custom':
          keys.push({
            text: 0,
            theme: ['middle']
          }, {
            text: this.extraKey,
            type: 'extra'
          });
          break;
      }

      return keys;
    },
    deleteText: function deleteText() {
      return this.deleteButtonText || t('delete');
    }
  },
  methods: {
    onBlur: function onBlur() {
      this.show && this.$emit('blur');
    },
    onClose: function onClose() {
      this.$emit('close');
      this.onBlur();
    },
    onAnimationEnd: function onAnimationEnd() {
      this.$emit(this.show ? 'show' : 'hide');
    },
    onPress: function onPress(text, type) {
      if (text === '') {
        return;
      }

      var value = this.value;

      if (type === 'delete') {
        this.$emit('delete');
        this.$emit('update:value', value.slice(0, value.length - 1));
      } else if (type === 'close') {
        this.onClose();
      } else if (value.length < this.maxlength) {
        this.$emit('input', text);
        this.$emit('update:value', value + text);
      }
    },
    genTitle: function genTitle() {
      var h = this.$createElement;
      var title = this.title,
          theme = this.theme,
          closeButtonText = this.closeButtonText;
      var titleLeft = this.slots('title-left');
      var showClose = closeButtonText && theme === 'default';
      var showTitle = title || showClose || titleLeft;

      if (!showTitle) {
        return;
      }

      return h("div", {
        "class": [bem('title'), BORDER_TOP]
      }, [titleLeft && h("span", {
        "class": bem('title-left')
      }, [titleLeft]), title && h("span", [title]), showClose && h("span", {
        "attrs": {
          "role": "button",
          "tabindex": "0"
        },
        "class": bem('close'),
        "on": {
          "click": this.onClose
        }
      }, [closeButtonText])]);
    },
    genKeys: function genKeys() {
      var _this = this;

      var h = this.$createElement;
      return this.keys.map(function (key) {
        return h(Key, {
          "key": key.text,
          "attrs": {
            "text": key.text,
            "type": key.type,
            "theme": key.theme
          },
          "on": {
            "press": _this.onPress
          }
        }, [key.type === 'delete' && _this.slots('delete'), key.type === 'extra' && _this.slots('extra-key')]);
      });
    },
    genSidebar: function genSidebar() {
      var h = this.$createElement;

      if (this.theme === 'custom') {
        return h("div", {
          "class": bem('sidebar')
        }, [this.showDeleteKey && h(Key, {
          "attrs": {
            "text": this.deleteText,
            "type": "delete",
            "theme": DELETE_KEY_THEME
          },
          "on": {
            "press": this.onPress
          }
        }, [this.slots('delete')]), h(Key, {
          "attrs": {
            "text": this.closeButtonText,
            "type": "close",
            "theme": CLOSE_KEY_THEME
          },
          "on": {
            "press": this.onPress
          }
        })]);
      }
    }
  },
  render: function render() {
    var h = arguments[0];
    return h("transition", {
      "attrs": {
        "name": this.transition ? 'van-slide-up' : ''
      }
    }, [h("div", {
      "directives": [{
        name: "show",
        value: this.show
      }],
      "style": {
        zIndex: this.zIndex
      },
      "class": bem([this.theme, {
        unfit: !this.safeAreaInsetBottom
      }]),
      "on": {
        "touchstart": stopPropagation,
        "animationend": this.onAnimationEnd,
        "webkitAnimationEnd": this.onAnimationEnd
      }
    }, [this.genTitle(), h("div", {
      "class": bem('body')
    }, [this.genKeys(), this.genSidebar()])])]);
  }
});