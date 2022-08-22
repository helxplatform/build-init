## Build Init

This repo contains source for an initialization container that can be invoked as 
part of the build pod using Kaniko invoked by Jenkins.  In particular, it works
around some behavior of the Kaniko executor when using a non stardard kanikodir.
