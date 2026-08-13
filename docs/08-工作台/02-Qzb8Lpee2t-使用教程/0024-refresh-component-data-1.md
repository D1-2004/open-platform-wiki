---
title: "刷新组件数据"
source_url: "https://open.dingtalk.com/document/dingstart/refresh-component-data-1"
namespace: "dingstart"
slug: "refresh-component-data-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例 > 刷新组件数据"
doc_id: "jKl2q6U1Md"
updated_at: "2025-09-03 15:57:12"
---

> Source: https://open.dingtalk.com/document/dingstart/refresh-component-data-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例 > 刷新组件数据
> Updated: 2025-09-03 15:57:12

# 刷新组件数据

组件里不允许进行轮询，因为工作台是个常驻小程序，未正确清理的轮询可能造成内存泄漏引起工作台崩溃。

## 示例

如果需要刷新数据，可以监听页面 **onShow** 事件，该事件会在工作台首页非首次展现出来时触发。

```
import { getSdk, getLifecycleSdk, } from '../../api/sdk';

Component({
    didMount() {
        getLifecycleSdk().didMount(this.props.componentName);
        // 初次渲染时获取一次数据
        this.fetchData();

      	/*
          事件绑定的函数需要明确this指向。
          如果写成listenCustomEvent('onShow', this.fetchData) 的话，
          在fetchData方法中获取到this已经不在当前作用域，所以要bind一下
        **/
      	this.refreshData = this.fetchData.bind(this);
        getSdk().listenCustomEvent('onShow', this.refreshData);
    },
    didUnmount() {
        getLifecycleSdk().didUnmount(this.props.componentName);
        // 由于didMount可能会触发多次，因此需要在didUnmount时清理绑定的事件
      	// 其次如果模块销毁时没有清除事件监听，可能会造成内存泄漏
        getSdk().removeCustomEvent('onShow', this.refreshData);
    },
    method: {
        async fetchData() {
            const data = await getSdk().request(this.props.componentProps.gateWayApi, {});
            ...
        }
    },
});
```

## onShow 事件触发机制

> **[!IMPORTANT]**
>
> 由于 **onShow** 触发频率较高可能对服务端产生压力，请谨慎评估需要用到本 SDK 的场景。

- 首次进入工作台时不会触发。
- 再次切换到工作台时触发。

  例如：钉钉底下 tab 切换到聊天，再切换到工作台时触发。在工作台上打开应用，再关闭应用回到工作台时触发。
