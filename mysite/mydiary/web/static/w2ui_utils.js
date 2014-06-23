var w2ui_uitls=function (w2uiObject) {
   this.uiObj=w2uiObject;
}

w2ui_uitls.prototype.addHandler=function(componentType,componentObj,targetItem,handleType,handler){
    var destComponents=this.uiObj[componentObj];
	if(!!destComponents){
		if(!!destComponents["on"+handleType]){
		  
		}
	}else{
		throw new Exception("could not find the wediget with name:"+componentObj);
	}
};

w2ui_utils.prototype.loadTableData=function(gridTable,records){
   var __records=[];
   if(!!girdTable.reload){
    __records=records;
	gridTable.reload();
   }  
}