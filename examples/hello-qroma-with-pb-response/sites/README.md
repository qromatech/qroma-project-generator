# Websites for your Qroma project


## Getting Started

Since the worldwide web is such a ubiquitous platform, web app development is constantly evolving and updating. As such, there are a lot of development tools to choose from, so we're going to give you a couple of templates that are driven by the commands, configurations, and states defined via your `device-io`.

However, nothing will prevent you from customization, since one of the benefits of many web development practices is that most tools will give you generally good defaults, but let you get under the hood and customize everything if that's what is necessary.

As such, learning to write web apps is out of the scope of Qroma projects, but we give you enough framework to have a comprehensive, full-featured starting point.


## Rationale

There are two types of sites to consider for a Qroma project.
* Published websites - These can host project information and provide a user interface for the devices (when plugged in to a PC or laptop). We recommend [Docusaurus](https://docusaurus.io/) because of its focus on documentation (which is important for a technical project), support for Markdown and Markdown with JSX (MD/MDX), and the ability to create/host your own react components, and flexibility. These sites can be published as static web apps and use USB/serial to bootstrap a plugged in embedded device as well as do full device control, configuration, and monitoring (depending on your project's settings).
* Device-hosted websites - These are websites that the device itself hosts so browsers on the same WiFi network can directly interact with it.