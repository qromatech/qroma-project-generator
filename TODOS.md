# Ideas to implement
#### For out of the box qroma projects (after site running, firmware installed on device, nothing else)
* Default qroma routes with "usable" UIs that handle
  * ~~Filesystem: basic~~
  * Changing update configuration
    * log level 
    * log/response type (e.g. progress indicator, counter - see `updateConfiguration.updateType` in firmware)
    * update interval
    * persisting these changes?
#### Full-fledged example projects
* Onboard pixel color changes per board in a single project
  * qroma-boards-demo
    * TinyPico
    * QTPy
    * website interaction
    * Python app interaction
* qromatech.com replacement
  * support TinyPico Qroma strips
  * support QTPy Qroma strips
  * include board hardware files
* Frank Hat 
  * custom image generation
  * includes hardware organization
#### More app/Python testing/integration
* monitoring scenarios
* large file scenarios
#### Qroma app infrastructure
* startup files
  * command mapping
* qroma points
  * configuration
  * Bluetooth mapping
* Bluetooth integration/mapping to commands