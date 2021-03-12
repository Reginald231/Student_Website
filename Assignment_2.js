var count = 0;
var rowArray = [];
var deletedRecordData = ""

var record = { //A holder for main pieces of data from a cell.
  row: "",
  c1Counter: "",
  c2Input: "",
  c3Label:""
}

//Adding a new cell to the table using nested "divs"
function addCell() {
  count++
  console.log("working");
  var table = document.getElementById("myTable")
  var baseDiv = document.createElement("div")

  var tableRow = document.createElement("rTableRow")

  console.log("increased.")
  var cellDiv = document.createElement("div")

  var cell1 = document.createElement("rTableCell")
  cell1Counter = document.createElement("label")
  cell1Counter.textContent = count-1;
  cell1.appendChild(cell1Counter)
  cellDiv.appendChild(cell1)

  var cell2 = document.createElement("rTableCell")
  cell2Input = document.createElement("input")
  cell2.type = "text/html"
  cell2.appendChild(cell2Input)
  cellDiv.appendChild(cell2)

  var cell3 = document.createElement("rTableCell")
  cell3Label = document.createElement("label")
  cell3Label.textContent = ""
  cell3.appendChild(cell3Label)
  cellDiv.appendChild(cell3)

  tableRow.appendChild(cellDiv)
  baseDiv.appendChild(tableRow)
  table.appendChild(baseDiv)

  var record = {
    row: tableRow,
    c1Counter: cell1Counter,
    c2Input: cell2Input,
    c3Label: cell3Label,
    c1: cell1,
    c2: cell2,
    c3: cell3
  }
  // record.c2Input.onchange = updateLength(this)
  rowArray.push(record)

  var el = record.c2Input;
  // Adding an event to each input field to enable real time length calculations
  el.addEventListener('keydown', (event) => {
  record.c3Label.textContent = record.c2Input.value.length+1;
});
}

function removeCell() {
  var table = document.getElementById("myTable")
  parent = table.getElementsByTagName("rTableRow")[0]
  var child = table.getElementsByTagName("div")[0]
  console.log(child)
  if (count > 1){
    table.removeChild(child);
    count--;
  }
  rowArray.pop()
}

// Using rowArray, sort the cells from greatest to least via comparing length.
/* Moving the actual elements in rowArray may be complicated.
 Alter the data within to keep things easier to read?
*/
function sortCells(){
  for (var i = 0; i < rowArray.length - 1; i++){
    for (var j = i+1; j < rowArray.length; j++){
      if (rowArray[i].c2Input.value.length < rowArray[j].c2Input.value.length){
        var tempC2Input = rowArray[j].c2Input.value
        var tempC3Label = rowArray[j].c3Label.textContent
        // var temp = rowArray[j]
        rowArray[j].c2Input.value = rowArray[i].c2Input.value
        rowArray[j].c3Label.textContent = rowArray[i].c3Label.textContent

        rowArray[i].c2Input.value = tempC2Input
        rowArray[i].c3Label.textContent = tempC3Label
      }
    }
  }

  // Printing resulting sorted array in the console.
  for(var i = 0; i < rowArray.length; i++){
    console.log(rowArray[i].c2Input.value + "\n" + rowArray[i].c3Label.textContent)
  }
}

function squareNumber() {
  var inputNum = document.getElementById("squaring").value
  var num = parseInt(inputNum, 10)
  var result = Math.pow(num, 2)
  resultString = "The result of the squaring of the number, " + inputNum +
    ", is " + result + "."
  alert(resultString)
  console.log(resultString)
}

/*THE FUNCTIONS BELOW ARE FOR ASSIGNMENT_2 PART 1.*/

function fixStart() {
  var inputString = document.getElementById("letterCheck").value.toLowerCase()
  var startChar = inputString.charAt(0)
  var subString = inputString.substring(1, inputString.length)
  var reg = new RegExp(startChar, "g")
  subString = subString.replace(reg, "*")
  var newString = startChar + subString

  alertString = "The initial string was '" + inputString + "'. The new string is '" +
    newString + "'."

  alert(alertString)
  console.log(alertString)
}

function notBad() {
  var sentence = document.getElementById("notBad").value.toLowerCase()
  var sentenceArray = sentence.split(" ")
  console.log(sentenceArray)

  notIndex = checkNot(sentenceArray)
  badIndex = checkBad(sentenceArray)
  console.log("Not index: " + notIndex)
  console.log("Bad index: " + badIndex)

  /*We just need to replace what is between "not" and "bad" (inclusive) with
  "good." if the word "not" comes before "bad" in the sequence. All other cases
  are ignored.*/
  if (notIndex < badIndex) {
    var i = badIndex
    for (i; i > notIndex; i--) {
      sentenceArray.splice(i, 1)
    }
    sentenceArray[i] = sentenceArray[i].replace("not", "good")
    resultString = ""
    for (var i = 0; i < sentenceArray.length; i++) {
      resultString += sentenceArray[i] + " "
    }
    alert(resultString)
    console.log("The new sentence is '" + resultString + "'.")
  }
}

/*checkNot and checkBad are helping functions for notBad. Searching for their
respective keywords: "bad" or "not."*/
function checkNot(sentenceArray) {
  for (var i = 0; i < sentenceArray.length; i++) {
    if (sentenceArray[i].includes("not")) {
      return i
    }
  }
  return "none"
}

function checkBad(sentenceArray) {
  for (var i = 0; i < sentenceArray.length; i++) {
    if (sentenceArray[i].includes("bad")) {
      return i
    }
  }
  return "none"
}
