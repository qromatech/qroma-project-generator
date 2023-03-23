# qroma-project-template

## What is _qroma_?

Qroma is a Device Project System (DPS) for documenting and developing embedded systems (both software and hardware aspects) so developers focus on convention over configuration (popularized by Ruby on Rails a long time ago) for user and device interaction. Embedded devices have state and can respond to user intentions. Users have multiple platforms and connectivity options that could potentially connect to those embedded devices. 

The less the embedded device developer has to worry about those distinctions early in the development process, the better. How those devices receive intentions and share states should be a function of what's in the messages themselves (size permitting, of course).

Qroma's ambitious goal is to make "Hello World" across devices and UX as frictionless as possible so that iteration and feedback can start happening across devices across the world in the first five minutes of your project. 

Its opinionated approach is based on development experiences across a range of embedded and UX platforms and a desire to priotize development and prototyping speed so that external feedback can be validated or invalidated, synthesized, and integrated into the next iteration of the project, either through user reports or direct pull requests.


## What is a _qroma_ project?

I am software developer who has been developing embedded software systems to assist performances that focus on visual effects (e.g. karate demonstrations, orchestra performances, cos-play effects). As my projects went on, there was more and more "stuff" to keep track of...
* Software
  * Embedded app repositories
  * Smartphone app repositories
  * Web app repositories
  * Shared libraries for type-system (e.g. Protocol buffers)
  * Shared integration testing repositories
  * Deployment procedures for each of the above
* Electronics
  * Schematics
  * Printed circuit board files
* Enclosures/Physical
  * Design schematics (e.g. part definitions)
  * STL/gcode files for 3D printing
* Overall Project Management
  * Bill of Materials and Parts List
  * Links to Parts
  * Assembly/integration documentation

The first part of this journey is to enable the hobbyist, Maker, and small-run manufacturer to be able to quickly/frictionlessly develop their embedded software project and its physical components and share it with/make it accessible to potential users in the medium that suits the user best (webpage, smartphone, smartwatch). If the developer follows some conventions (with the ability to override with configurations) with their device user interface interactions (e.g. commands/responses/settings), a serviceable user interface can be available on a wide range of devices with little or no effort. Customizability would be available as desired, but the no-frills interfaces should not require any extra effort, which is key for rapid iteration.

We need infrastructure and development/tooling processes that are secure and reliable, but focus on the prototyper’s software development practices and cycles that focus on getting end-user engagement and quick feedback. Product end-users would benefit from shared/common development practices (and subsequent user interface improvements and convergence) and an internet infrastructure that would support sharing of common configurations and streamline project improvements.


## Why does this project template exist? 

The ambitious goal of the qroma project is to bring together the pieces required for a successful embedded project in one place so that developers and Makers can focus on the problems they are solving and the value they are delivering to the users of their devices. Like Ruby on Rails let developers focus on "business logic" using convention over configuration, a Qroma project lets its users focus on what its device "does" and its connections to the outside world rather than on the mechanisms of how that all works. Nothing should prevent configuration overrides when the conventions aren't working out, but we're hopeful bringing everything together will be useful enough for enough people that this can become another avenue prototypes can take on their way to becoming products.

Authors of instructional and HOW TO material for embedded electronics projects shouldn't need to don’t need to tell people to download Arduino, check out a git repository, and go through software compile/build steps to get a _Hello World_ project working. With a qroma project, it should be simple for the author to do those steps on their machine, package it up and publish it (maybe with some configuration), and get their audience to reproduce their results without spending several paragraphs trying to get their audience to follow build steps.

The first versions will enable hobbyists and prototypers to quickly/frictionlessly develop an embedded software project and share it with/make it accessible to potential users in the medium that suits the user best (webpage, smartphone app, voice integration). If the prototyper follows some conventions (with the ability to override with configurations) with their device user interface interactions (e.g. commands/responses/settings), it should be feasible to get a serviceable user interface up and available on a wide range of devices with little or not effort. Customizability would be available as desired, but the no-frills interfaces should not require any extra effort, which is key for rapid iteration.

As a project creator, a statically generated project website that can compile, host, and present all of this information is very attractive, especially since archiving and sharing is critical to effective information sharing. When I do a prototype or a small-scale run, I want updates to be accessible online to interested testers and users and let them know. Additionally, versioning with git handles all sorts of revision control issues that are common to all file formats. Project level tags will keep points in time in sync so that managing complexity becomes more tractable.


## Deeper Dives

Further documentation is available for these topics:
* [Directory structure for projects](/DIRECTORY-LAYOUT.md)
* [Defining project-level device commands](/device-io/protobufs/README.md)
* [Setting up device projects and using embedded software development frameworks](/device-boards/README.md)
* [Documenting and hosting your Qroma project either on the Internet or on the device itself](/sites/README.md)
* [Using your Qroma devices from a smartphone](/apps/README.md)