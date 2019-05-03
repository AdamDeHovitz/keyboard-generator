var fs = require(['fs']);
var json2csv = require(['json2csv']);


var newLine= "\r\n";
var fields = ['Timestamp', 'Character'];

var filename = 'website_timings.csv'
function myFunction(event) {
  var x = event.which || event.keyCode;
  //document.getElementById("demo").innerHTML = "The Unicode value is: " + x;
  var appendThis = [
    {
        'Timestamp': '100',
        'Character': x
    },

	];
	var toCsv = {
	    data: appendThis,
	    fields: fields,
	    hasCSVColumnTitle: false
	};	

	fs.stat(filename, function (err, stat) {
    if (err == null) {
        console.log('File exists');

        //write the actual data and end with newline
        var csv = json2csv(toCsv) + newLine;

        fs.appendFile(filename, csv, function (err) {
            if (err) throw err;
            console.log('The "data to append" was appended to file!');
        });
    }
    else {
        //write the headers and newline
        console.log('New file, just writing headers');
        fields= (fields + newLine);

        fs.writeFile(filename, fields, function (err, stat) {
            if (err) throw err;
            console.log('file saved');
        });
    }
});
}










