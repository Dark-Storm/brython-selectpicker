from browser import document, html


class CustomSelect():

    default_value_trigger = "Выберите из списка"

    def __init__(self, target, live_search=False):
        self.target = target
        #self.target.width = 0
        self.live_search = live_search
        self.selectedIndex = self.target.selectedIndex
        print(self.selectedIndex)
        #print(self.target.options.selected)
        self.multiselectable = self.target.multiple
        self.data = self.get_data()
        self.initUIComponent()
        self.render()
        self.set_init_values()
        self.register_events()

    def initUIComponent(self):
        self.main_div = html.DIV(Class="select")
        self.dropdown = html.DIV(Class='select__dropdown')
        self.trigger = html.BUTTON(self.default_value_trigger, Class='select__trigger', **{'data-select': 'trigger'})
        self.listbox = self.get_listbox(self.data)
        #box = html.DIV(Class='search')
        self.search = html.INPUT(Class='form-control', type="search")
        self.backdrop = html.DIV(Class='select__backdrop', **{'data-select': 'backdrop'})
        
    def update_tigger(self):
        
        text = ""
        for item in self.listbox.select('.select__item_selected'):
            if text:
                text += "; " + item.text
            else:
                text = item.text
        if text:
            self.trigger.text = text
        else:
            self.trigger.text = self.default_value_trigger

    def register_events(self):

        self.trigger.bind('click', self.toogle)
        self.listbox.bind('click', self.change_value)
        self.backdrop.bind('click', self.hide_listbox)
        self.search.bind('input', self.filter_listbox)

    def setup_focus(self, event):
        target = event.target
        print(target)

    def filter_listbox(self, event):
        str_search = event.target.value
        listbox = self.get_listbox(self.filter_data(str_search))
        self.listbox.html = listbox.html

    def change_value(self, event):
        item = event.target
        self.set_value_item(item)
        self.update_tigger()
        if not self.multiselectable:
            self.hide_listbox(event)

    def set_init_values(self):
        self.init_values = {item.index for item in self.target.options if item.selected}
        if self.init_values:
            for item in self.listbox.select(".select__item"):
                if int(item.attrs.get("data-select")) in self.init_values:
                    self.set_value_item(item)
                    self.update_tigger()

    def set_value_item(self, item):
        if self.multiselectable:
            if item.classList.contains("select__item_selected"):
                item.classList.remove("select__item_selected")
                self.target.options[item.attrs.get("data-select")].selected = False
            else:
                item.classList.add("select__item_selected")
                self.target.options[item.attrs.get("data-select")].selected = True
        else:
            for prev_item in self.listbox.select(".select__item_selected"):
                prev_item.classList.remove("select__item_selected")
            item.classList.add("select__item_selected")
            item.attrs["aria-selected"] = "true"
            self.target.options[item.attrs.get("data-select")].selected = True
    
    def _is_show(self):
        if self.main_div.classList.contains("select_show"):
            return True
        else:
            return False
    
    def toogle(self, event):
        if self._is_show():
            self.hide_listbox(event)
        else:
            self.show_listbox()
    
    def show_listbox(self):
        self.dropdown.classList.add("select_show")
        self.dropdown.style = {"max-height": "327px", "overflow": "hidden", "min-height": "162px", "position": "absolute", "transform": "translate3d(0px, 31px, 0px)", "top": "0px", "left": "0px", "will-change": "transform"}
        self.main_div.classList.add("select_show")
        style = self.listbox.style
        style.maxHeight = "263px"
        style.overflowY = "auto"
        style.minHeight = "98px"
        try:
            self.listbox.select('.select__item_selected')[0].focus(preventScroll=False)
        except IndexError:
            pass

    def hide_listbox(self, event):
        self.dropdown.classList.remove("select_show")
        self.main_div.classList.remove("select_show")

    def render(self):
        self.dropdown <= html.DIV(self.search, Class='search')
        self.dropdown <= self.listbox
        
        self.main_div <= self.backdrop
        self.main_div <= self.trigger
        self.main_div <= self.dropdown
        self.target.parent.insertBefore(self.main_div, self.target)

    def get_data(self):
        return {item.index: item.text for item in self.target.options}
    
    def filter_data(self, search):
        return {key: value for key, value in self.data.items() if search.lower() in value.lower()}
    
    def get_listbox(self, data):
        div = html.DIV(Class="dropdown__inner")
        ul = html.UL(Class="select__items", **{"role": "presentation"})
        for index, item in data.items():
            li = html.LI(item, Class="select__item")
            li.attrs['data-select'] = index
            li.attrs['tabindex'] = "0"
            ul <= li
        div <= ul
        return div

#{k: v for k, v in d.items() if v > 0}
"""<div class="select">
          <div class="select__backdrop" data-select="backdrop"></div>
          <button type="button" class="select__trigger" data-select="trigger">
            Выберите из списка
          </button>
          <div class="select__dropdown">
            <div class="searchbox">
              <input type="search" class="form-control" data-select="search">
            </div>
            <ul class="select__items">
              <li class="select__item" data-select="item">1</li>
              <li class="select__item select__item_selected" data-select="item">2</li>
              <li class="select__item" data-select="item">3</li>
              <li class="select__item" data-select="item">4</li>
              <li class="select__item" data-select="item">5</li>
              <li class="select__item" data-select="item">6</li>
              <li class="select__item" data-select="item">7</li>
              <li class="select__item" data-select="item">8</li>
              <li class="select__item" data-select="item">9</li>
            </ul>
          </div>
        </div>"""

for select_item in document.select(".brython_select"):
    CustomSelect(select_item)