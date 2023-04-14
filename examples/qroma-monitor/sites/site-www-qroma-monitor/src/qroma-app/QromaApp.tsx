import React from "react"
import { HelloQromaRequest, MathRequest, QromaHeartbeatUpdate } from "../qroma-proto/qroma-monitor";
import { QromaUpdateMonitor } from "./QromaUpdateMonitor";
// import { QromaRequest } from "../qroma-lib/QromaRequest";
import { QromaRequest } from 'react-qroma/src/qroma-lib/QromaRequest'
import { reactQromaFn123 } from 'react-qroma'


export const QromaApp = () => {

  reactQromaFn123();

  return <div>
    Qroma App

    <QromaUpdateMonitor
      messageType={QromaHeartbeatUpdate}
      />

    <QromaRequest
      messageType={HelloQromaRequest}
      />
    <QromaRequest
      messageType={MathRequest}
      />
  </div>
}