
chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        if( details.url == "https://inventory.labarchives.com/printers/DYMO.Printers.js" )
            return {redirectUrl: "https://github.com/lbcai/simple-tools/printExtension/replaced.Printers.js" };
    },
    {urls: ["https://inventory.labarchives.com/printers/DYMO.Printers.js"]},
    ["blocking"]);
