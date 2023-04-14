import React, { useState } from "react"
import { MessageType } from "@protobuf-ts/runtime";
import { QromaRequestForm } from "react-qroma";
import { QromaCommMonitor } from 'react-qroma';


interface IQromaCommandDeviceAppProps<T extends object, U extends object> {
  requestMessageType: MessageType<T>
  responseMessageType: MessageType<U>
}


export const QromaCommandDeviceApp = <T extends object, U extends object>(props: IQromaCommandDeviceAppProps<T, U>) => {
  
  const [response, setResponse] = useState("NOT SET");
  
  return (
    <>
      {props.requestMessageType.typeName} =&gt; {props.responseMessageType.typeName}

      <div>
        {response}
      </div> 

      <QromaRequestForm
        requestMessageType={props.requestMessageType}
        />

      <QromaCommMonitor
        messageType={props.responseMessageType}
        />
    </>
  )
}