chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        if( details.url == "https://inventory.labarchives.com/printers/DYMO.Printers.js" )
            return {redirectUrl: "file:///replaced.Printers.js" };
    },
    {urls: ["https://inventory.labarchives.com/printers/DYMO.Printers.js"]},
    ["blocking"]);