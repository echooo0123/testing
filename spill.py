element_info = '{"html":{"tagName":"PRE","attrMap":{"tag":"PRE","css-selector":"body>div>div>div>div>div>div>div>div>div>div>div>div>div>div>div>div>div>pre"},"index":0},"wnd":[{"app":"chrome","cls":"Chrome_WidgetWin_1","title":"*"},{"cls":"Chrome_RenderWidgetHostHWND","title":"Chrome Legacy Window"}]}'

import json

# 解析JSON字符串
data = json.loads(element_info)

# 获取XPath属性
xpath = data['html']['attrMap']['css-selector']

print(xpath)
