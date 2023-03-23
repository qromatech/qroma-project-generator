# Embedded Boards and Platforms

## Getting Started

The main requirement for these embedded board/platform projects is to create a binary image that can be uploaded to the relevant boards using whatever upload tools are available and configured.

When you are starting your project, your commands, configuration, and states should be defined in `$PROJECT_ROOT/device-io/protobufs/protofiles-in` ([see details here](../device-io//protobufs/README.md)). Once that is done and you've compiled your Protocol Buffer definitions, the `struct` and other type definitions will be available to our Arduino/PlatformIO projects so we can start handling their implementations right away.

Go to the embedded device project in `$PROJECT_ROOT/device-boards` and open it up with an appropriate editor. At this point, you can write your own device code, ideally focusing on handling commands and returning responses, not in writing any communication boilerplate code!

## Rationale

There's not a lot to add for the embedded device development experience, other than to integrate it nicely with the Protocol Buffer command definitions using Qroma libraries to handle communication abstractions across the different communication mediums. We're going to make intelligent default selections, keep the bindings as unopinionated as possible, giving you the option to eject or refactor later without having to replace logic.

As for project/code editors, use whatever you're comfortable with. At some point, we might express a preference, but there's lot of documentation out there and we don't think getting hung up on a device compiler/delivery mechanism makes much sense.

Platforms we have experience with and will keep working towards include:
* Arduino
* PlatformIO
* MicroPython