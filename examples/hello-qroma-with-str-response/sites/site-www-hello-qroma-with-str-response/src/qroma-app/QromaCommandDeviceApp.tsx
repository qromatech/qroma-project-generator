import React from "react"
import { MessageType } from "@protobuf-ts/runtime";
import { QromaRequestForm } from "react-qroma";
import { QromaStrMonitor } from "./QromaStrMonitor";


interface IQromaCommandDeviceAppProps<T extends object, U extends object> {
  requestMessageType: MessageType<T>
}


export const QromaCommandDeviceApp = <T extends object, U extends object>(props: IQromaCommandDeviceAppProps<T, U>) => {
  

  return (
    <>
      {props.requestMessageType.typeName} =&gt; RESPONSE STR
      
      <QromaRequestForm
        requestMessageType={props.requestMessageType}
        />
        
      {/* <QromaAppRequestForm
        requestMessageType={props.requestMessageType}
        /> */}


      <QromaStrMonitor
        />
    </>
  )
}