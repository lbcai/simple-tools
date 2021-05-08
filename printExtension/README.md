# printExtension
Google Chrome extension to allow the LabArchives Inventory label printing and scanning system to be used with label formats other than the default. The system is limited in that it is only compatible with DYMO printers and a specific type of cryolabel. This extension currently allows the system to also use 1.04" x 0.5" cryolabels with spot by Labtag.

## Usage
Download the files and add the root folder to Chrome as an extension in Developer Mode. No other action is necessary. The extension will automatically block the default LabArchives label template and replace it with a custom one. The extension only functions on LabArchives sites.

## Possible Future Features
These features may not actually be feasible due to restrictions. Feasibility is to be determined.
* UI that allows user to specify label dimensions and other technical details
* Function that allows user to use label printers other than DYMO's (may require tricking LabArchives into thinking a DYMO is connected, then intercepting print instructions and translating for the new printer)
