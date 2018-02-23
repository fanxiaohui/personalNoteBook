#!/bin/bash
for i in $(grep -l "PsCommon/ActiveCellSRS" *.rtm)
  do
    sed -i "/require.*ActiveCellSRS/c require PsCommon/ActiveCell" $i
    sed -i "/require.*ActiveCell/a require PsCommon/ConfigCellSRS" $i 
  done

echo "done"



////////////////////////
这个脚本的功能是：在当前目录下所有的rtm文件中查找包含内容 PsCommon/ActiveCellSRS 的文件，并修改这些文件的内容：
1）替换require  PsCommon/ActiveCellSRS 为 require PsCommon/ActiveCell
2) 替换后追加一行 require PsCommon/ConfigCellSRS
