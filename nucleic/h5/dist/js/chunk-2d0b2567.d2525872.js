(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0b2567"],{"244c":function(e,o,t){"use strict";t.r(o);var l=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",[t("van-nav-bar",{attrs:{title:"核酸检测预约登记",fixed:"","safe-area-inset-top":"",placeholder:""}}),t("van-form",{on:{submit:e.doSubmit}},[t("van-cell-group",[t("van-cell",{attrs:{"is-link":"",title:"证件类别",value:e.form.zjlb},on:{click:function(o){e.options.zjlb.show=!0}}}),t("van-action-sheet",{attrs:{actions:e.options.zjlb.actions},on:{select:e.onZjlbSelect},model:{value:e.options.zjlb.show,callback:function(o){e.$set(e.options.zjlb,"show",o)},expression:"options.zjlb.show"}}),t("van-field",{attrs:{label:"证件号码",placeholder:"请输入证件号码",required:"",rules:[{required:!0,message:"请填写证件号码"}]},scopedSlots:e._u([{key:"button",fn:function(){return[t("van-button",{attrs:{size:"small",plain:""},on:{click:e.doScan}},[t("van-icon",{attrs:{name:"photo-o"}})],1)]},proxy:!0}]),model:{value:e.form.zjhm,callback:function(o){e.$set(e.form,"zjhm",o)},expression:"form.zjhm"}}),t("van-field",{attrs:{label:"姓名",placeholder:"请输入姓名",required:"",rules:[{required:!0,message:"请填写姓名"}]},model:{value:e.form.xm,callback:function(o){e.$set(e.form,"xm",o)},expression:"form.xm"}}),t("van-cell",{staticClass:"xb",staticStyle:{"text-align":"left"},attrs:{title:"性别"}},[t("van-radio-group",{attrs:{direction:"horizontal"},model:{value:e.form.xb,callback:function(o){e.$set(e.form,"xb",o)},expression:"form.xb"}},[t("van-radio",{attrs:{name:"1",shape:"square"}},[e._v("男")]),t("van-radio",{attrs:{name:"2",shape:"square"}},[e._v("女")])],1)],1),t("van-field",{attrs:{label:"电话",placeholder:"请输入11位手机号",required:"",rules:[{required:!0,message:"请填写电话"}]},model:{value:e.form.lxdh,callback:function(o){e.$set(e.form,"lxdh",o)},expression:"form.lxdh"}}),t("van-field",{attrs:{label:"年龄",placeholder:"请输入年龄"},model:{value:e.form.nl,callback:function(o){e.$set(e.form,"nl",o)},expression:"form.nl"}}),t("van-field",{attrs:{label:"户籍地址",placeholder:"请输入身份证上的户籍地址"},model:{value:e.form.hjdz,callback:function(o){e.$set(e.form,"hjdz",o)},expression:"form.hjdz"}}),t("van-field",{attrs:{label:"居住地址",placeholder:"请输入您的现住址",required:"",rules:[{required:!0,message:"请填写居住地址"}]},model:{value:e.form.jzdz,callback:function(o){e.$set(e.form,"jzdz",o)},expression:"form.jzdz"}}),t("van-field",{attrs:{label:"工作单位",placeholder:"请输入您的工作单位"},model:{value:e.form.dw,callback:function(o){e.$set(e.form,"dw",o)},expression:"form.dw"}}),t("van-field",{attrs:{label:"体温",placeholder:"请输入您目前体温"},model:{value:e.form.tw,callback:function(o){e.$set(e.form,"tw",o)},expression:"form.tw"}}),t("van-field",{attrs:{label:"备注",placeholder:"其他备注信息"},model:{value:e.form.bz,callback:function(o){e.$set(e.form,"bz",o)},expression:"form.bz"}})],1),t("div",{staticStyle:{margin:"1rem"}},[t("van-button",{attrs:{round:"",block:"",type:"info","native-type":"submit"}},[e._v("提交")])],1)],1)],1)},a=[],n=(t("ac1f"),t("5319"),t("b0c0"),t("365c")),r=t("1602"),s={data:function(){return{form:{djrq:"",zjlb:"身份证",zjhm:"",xm:"",xb:"1",lxdh:"",nl:"",nldw:"年",hjdz:"",jzdz:"",dw:"",tw:"",bz:""},options:{zjlb:{show:!1,actions:[{name:"身份证"},{name:"户口本"},{name:"护照"}]}}}},mounted:function(){this.form.djrq=new Date,this.loadQrCode()},methods:{loadQrCode:function(){var e=window.localStorage.getItem("personInfo");e&&this.$router.replace("/qrcode")},doScan:function(){var e=this,o={zjhm:Object(r["a"])(),xb:"1",xm:"三酷猫",nl:"35",hjdz:"贝克街211B",csrq:"1986-10-10 00:00:00"};this.$dialog.alert({message:"原系统中，调起摄像头拍摄身份证信息，使用”百度证件识别API“，将识别结果填入页面，本系统使用模拟数据演示功能"}).then((function(){Object.assign(e.form,o),window.localStorage.setItem("v-card-id",o.zjhm)}))},onZjlbSelect:function(e){this.options.zjlb.show=!1,this.form.zjlb=e.name},doSubmit:function(){var e=this;Object(n["e"])(this.form).then((function(o){window.localStorage.setItem("personInfo",JSON.stringify(o)),e.$router.push("/qrcode")}))}}},i=s,c=t("2877"),d=Object(c["a"])(i,l,a,!1,null,null,null);o["default"]=d.exports}}]);