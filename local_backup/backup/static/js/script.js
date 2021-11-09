var dropZoneId = "drop-zone";
var buttonId = "clickHere";
var uploadButton = "upload";
var mouseOverClass = "mouse-over";
var dropZone = $("#" + dropZoneId);
var ooleft = dropZone.offset().left;
var ooright = dropZone.outerWidth() + ooleft;
var ootop = dropZone.offset().top;
var oobottom = dropZone.outerHeight() + ootop;
var inputFile = dropZone.find("input");
var finalFiles = new Array()

function updateFileNameDisplayArea(){
    $('#filename').html('')
    var fileNum = finalFiles.length;
    var initial = 0;
    console.log(fileNum)
    for (initial; initial < fileNum; initial++) {
        console.log(finalFiles[initial]);
        $('#filename').append(
            '<span class="fa-stack fa-lg">\
                <i class="fa fa-file fa-stack-1x "></i>\
                <strong class="fa-stack-1x" style="color:#FFF; font-size:12px; margin-top:2px;">'
                + (initial+1) +
                '</strong>\
            </span> ' 
            + finalFiles[initial].name + 
            '&nbsp;&nbsp;<span class="fa fa-times-circle fa-lg closeBtn" title="remove" onClick="deleteRow('+ initial + ')">\
            </span><br>'
        );
    }
}

function deleteRow(index){
    console.log(index)
    finalFiles.splice(index, 1);
    updateFileNameDisplayArea()
}

$(function () {

    document.getElementById(dropZoneId).addEventListener("dragover", function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropZone.addClass(mouseOverClass);
        var x = e.pageX;
        var y = e.pageY;

        if (!(x < ooleft || x > ooright || y < ootop || y > oobottom)) {
            inputFile.offset({
                top: y - 15,
                left: x - 100
            });
        } else {
            inputFile.offset({
                top: -400,
                left: -400
            });
        }

    }, true);

    if (buttonId != "") {
        var clickZone = $("#" + buttonId);

        var oleft = clickZone.offset().left;
        var oright = clickZone.outerWidth() + oleft;
        var otop = clickZone.offset().top;
        var obottom = clickZone.outerHeight() + otop;

        $("#" + buttonId).mousemove(function (e) {
            var x = e.pageX;
            var y = e.pageY;
            if (!(x < oleft || x > oright || y < otop || y > obottom)) {
                inputFile.offset({
                    top: y - 15,
                    left: x - 160
                });
            } else {
                inputFile.offset({
                    top: -400,
                    left: -400
                });
            }
        });
    }

    document.getElementById(dropZoneId).addEventListener("drop", function (e) {
        $("#" + dropZoneId).removeClass(mouseOverClass);
    }, true);

    inputFile.on('change', function (e) {
        var fileNum = this.files.length;
        var initial = 0;
        console.log(fileNum);
        for (initial; initial < fileNum; initial++) {
            finalFiles.push(this.files[initial])
        }
        console.log(finalFiles)
        updateFileNameDisplayArea()
    });

    document.getElementById(uploadButton).addEventListener("click", function(e) {
        
    })
	
})