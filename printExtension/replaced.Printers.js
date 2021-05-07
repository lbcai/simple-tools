function loadPrinters(printersSelect) {
  const printers = dymo.label.framework.getPrinters();
  if (!printersSelect || printers.length === 0) {
    throw new Error("Printers are not ready yet. Please try again.");
  }

  printers.forEach(printer => {
    if (printer.printerType === "LabelWriterPrinter") {
      const printerName = printer.name;
      if (!printersSelect.options || (printersSelect.options && !printersSelect.options.namedItem(printerName))) {
        const option = document.createElement("option");
        option.id = printerName;
        option.value = printerName;
        option.append(document.createTextNode(printerName));
        printersSelect.append(option);
      }
    }
  });
}

function getLabels() {
  return {
    defaultValue: 91386000,
    data: {
      91386000: {
        desciption: `DTCR 9138-6000 (Combo Label) (1.50 x 0.50, 0.375 dia spot)`,
        printLabel: printDymo91386000,
      },
      // 30252: {
      //   desciption: `DYMO 30252 Address (3.5 x 1.125)`,
      //   printLabel: printDymo30252,
      // },
    },
  };
}

function printLabel(labelValue, printerValue, png1, png2) {
  if (labelValue && printerValue && png1 && png2) {
    getLabels().data[labelValue].printLabel(printerValue, png1, png2);
  }
}

function printDymo30252(printerValue, addressPng) {
  const labelPng = dymo.label.framework.openLabelXml(getDymo30252Label());

  if (addressPng && printerValue) {
    labelPng.setObjectText("Image", addressPng);
    labelPng.print(printerValue);
  }
}

function getDymo30252Label() {
  return `<?xml version="1.0" encoding="utf-8"?>
  <DieCutLabel Version="8.0" Units="twips">
      <PaperOrientation>Landscape</PaperOrientation>
      <Id>Address</Id>
      <PaperName>30252 Address</PaperName>
      <DrawCommands>
          <RoundRectangle X="0" Y="0" Width="1581" Height="5040" Rx="270" Ry="270" />
      </DrawCommands>
      <ObjectInfo>
          <ImageObject>
              <Name>Image</Name>
              <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
              <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
              <LinkedObjectName></LinkedObjectName>
              <Rotation>Rotation0</Rotation>
              <IsMirrored>False</IsMirrored>
              <IsVariable>False</IsVariable>
              <ImageLocation/>
              <ScaleMode>Fill</ScaleMode>
              <BorderWidth>0</BorderWidth>
              <BorderColor Alpha="255" Red="0" Green="0" Blue="0" />
              <HorizontalAlignment>Left</HorizontalAlignment>
              <VerticalAlignment>Top</VerticalAlignment>
          </ImageObject>
          <Bounds X="332" Y="150" Width="4455" Height="1260" />
      </ObjectInfo>
  </DieCutLabel>`;
}

function printDymo91386000(printerValue, longPng, circlePng) {
  const labelPng = dymo.label.framework.openLabelXml(getDymo91386000Label());

  if (longPng && circlePng && printerValue) {
    labelPng.setObjectText("LongPng", longPng);
    labelPng.setObjectText("CirclePng", circlePng);
    labelPng.print(printerValue);
  }
}

function getDymo91386000Label() {
  return `<?xml version="1.0" encoding="utf-8"?>
  <DieCutLabel Version="8.0" Units="twips">
    <PaperOrientation>Portrait</PaperOrientation>
    <Id>DT Cryo-Tag DTCR-6000 1.50" x 0.50" w/3/8" Spot</Id>
    <IsOutlined>false</IsOutlined>
    <CustomPaper>
      <Size Width="1260" Height="3600" />
      <PrintableSize Width="720" Height="3600" />
      <PrintableOrigin X="0" Y="0" />
      <Offset X="350" Y="-400" />
    </CustomPaper>
    <DrawCommands>
      <RoundRectangle X="0" Y="540" Width="720" Height="2160" Rx="180" Ry="180" />
      <RoundRectangle X="70" Y="2740" Width="500" Height="500" Rx="270" Ry="270" />
    </DrawCommands>
    <ObjectInfo>
      <ImageObject>
        <Name>LongPng</Name>
        <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
        <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
        <LinkedObjectName></LinkedObjectName>
        <Rotation>Rotation90</Rotation>
        <IsMirrored>False</IsMirrored>
        <IsVariable>False</IsVariable>
        <ImageLocation/>
        <ScaleMode>Fill</ScaleMode>
        <BorderWidth>0</BorderWidth>
        <BorderColor Alpha="255" Red="0" Green="0" Blue="0" />
        <HorizontalAlignment>Center</HorizontalAlignment>
        <VerticalAlignment>Center</VerticalAlignment>
      </ImageObject>
      <Bounds X="40.5633802816901" Y="510.788732394366" Width="652.394366197183" Height="2051.83098591549" />
    </ObjectInfo>
    <ObjectInfo>
      <ImageObject>
        <Name>CirclePng</Name>
        <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
        <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
        <LinkedObjectName></LinkedObjectName>
        <Rotation>Rotation90</Rotation>
        <IsMirrored>False</IsMirrored>
        <IsVariable>False</IsVariable>
        <ImageLocation/>
        <ScaleMode>Uniform</ScaleMode>
        <BorderWidth>0</BorderWidth>
        <BorderColor Alpha="255" Red="0" Green="0" Blue="0" />
        <HorizontalAlignment>Center</HorizontalAlignment>
        <VerticalAlignment>Center</VerticalAlignment>
      </ImageObject>
      <Bounds X="170" Y="2800" Width="400" Height="400" />
    </ObjectInfo>
  </DieCutLabel>`;
}