// Select color input
function addColor (id) {
    color = document.querySelector("#colorPicker").value;
    box = document.getElementById(id);
    box.style.backgroundColor = color;
}
//makeGrid Function
function makeGrid(height,width) {
    html = ""
    for(var h = 1; h <= height; h++) 
    {
        html += "<tr>"
        for (var w = 1; w <= width; w++) 
        {
            html += '<td id=a'+h+w+' onclick=addColor(id) \
            style="border:2px solid black; height:25px; width: 25px"></td>';
        }
        html += "</tr>"
    }
    return html
}
// Select size input
var size = document.querySelector('#sizePicker');

size.querySelector('button').addEventListener('click', function() 
{
    var height = size.querySelector('#inputHeight').value;
    var width = size.querySelector('#inputWidth').value;

    var element = document.querySelector('table');
    element.parentNode.removeChild(element);

    var table = document.createElement("table");
    document.body.appendChild(table)
    table = document.body.querySelector('table');
    
    // When size is submitted by the user, call makeGrid()
    html = makeGrid(height,width);
    table.insertAdjacentHTML('afterbegin',html);
});
