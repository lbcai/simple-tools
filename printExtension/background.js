chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        if( details.url == "https://inventory.labarchives.com/printers/DYMO.Printers.js" )
            return {redirectUrl: "https://mynotebook.labarchives.com/attachments/MjMuNDAwMDAwMDAwMDAwMDAyfDcxNDU5Ni8xOC9FbnRyeVBhcnQvMzczOTUyOTc2Mnw1OS40/47/original" };
    },
    {urls: ["https://inventory.labarchives.com/printers/DYMO.Printers.js"]},
    ["blocking"]);