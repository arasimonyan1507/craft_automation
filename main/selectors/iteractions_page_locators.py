from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list>div>div.list-group-item.list-group-item-action")
    GRID_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-grid>div>div>div.list-group-item.list-group-item-action")


class SelectablePageLocators(SortablePageLocators):
    LIST_ITEMS = (By.CSS_SELECTOR, '#verticalListContainer>li.mt-2.list-group-item.list-group-item-action')
    GRID_ITEMS = (By.CSS_SELECTOR, '#gridContainer>div>li.list-group-item.list-group-item-action')
    LIST_SELECTED_ITEMS = (By.CSS_SELECTOR, '#verticalListContainer>li[class*="active"]')
    GRID_SELECTED_ITEMS =(By.CSS_SELECTOR, '#gridContainer>div>li[class*="active"]')


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, '#resizableBoxWithRestriction')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, '#resizableBoxWithRestriction>span[class^="react-resizable-handle"]')
    RESIZABLE = (By.CSS_SELECTOR, "#resizable")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, '#resizable>span[class^="react-resizable-handle"]')


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-simple")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#draggable')
    SIMPLE_DROP_ZONE = (By.CSS_SELECTOR, '#droppable')
    ACCEPT_TAG = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, "#acceptable")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "#notAcceptable")
    ACCEPT_DROP_ZONE = (By.CSS_SELECTOR, '#acceptDropContainer>#droppable>p')


class RevertDraggablePageLocators:
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    WILL_REVERT = (By.CSS_SELECTOR, "#revertable")
    NOT_REVERT = (By.CSS_SELECTOR, "#notRevertable")
    REVERTABLE_DROP = (By.CSS_SELECTOR, "#revertableDropContainer>#droppable>p")


class PreventPropogationPageLocators:
    PROPOGATION_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    NOT_GREEDY = (By.CSS_SELECTOR, "#notGreedyInnerDropBox")
    DRAG_ME = (By.CSS_SELECTOR, "#dragBox")


class DraggablePageLocators:
    # simple
    SIMPLE_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#dragBox')
    # axis
    AXIS_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-axisRestriction')
    RESTRICTED_X = (By.CSS_SELECTOR, "#restrictedX")
    RESTRICTED_Y = (By.CSS_SELECTOR, '#restrictedY')
    # restricted container
    RESTRICTED_CONTAINER_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-containerRestriction")
    CONTAINED_BOX = (By.CSS_SELECTOR, '#containmentWrapper>div[class^="draggable"]')
