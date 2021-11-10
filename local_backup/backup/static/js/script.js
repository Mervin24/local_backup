var dropZoneId = "drop-zone";
var buttonId = "clickHere";
var uploadButton = "upload";
var viewUploadsButton = "view-uploads"
var mouseOverClass = "mouse-over";
var dropZone = $("#" + dropZoneId);
var ooleft = dropZone.offset().left;
var ooright = dropZone.outerWidth() + ooleft;
var ootop = dropZone.offset().top;
var oobottom = dropZone.outerHeight() + ootop;
var inputFile = dropZone.find("input");
var finalFiles = new Array()
const POST = "POST"
const uploadedFiles = "uploadedFiles"
const uploadedFilesUrl = "file-upload"
const csrfmiddlewaretoken = 'csrfmiddlewaretoken'

function updateFileNameDisplayArea(){
    $('#filename').html('')
    var fileNum = finalFiles.length;
    var initial = 0;
    for (initial; initial < fileNum; initial++) {
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
    finalFiles.splice(index, 1);
    updateFileNameDisplayArea()
}

function uploadFileList(fileList){
    var formData = new FormData()
    for(var i = 0; i < fileList.files.length; i++){
        console.log(fileList.files[i])
        formData.append(uploadedFiles, fileList.files[i])
    }
    formData.append(csrfmiddlewaretoken, csrftoken);
    $.ajax({
        type: POST,
        url: uploadedFilesUrl,
        data: formData,
        success: function(data){
            console.log(data)
        },
        error: function(data){
            console.log(data)
        },
        async: true,

        contentType: false,
        processData: false,
    })
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
        for (initial; initial < fileNum; initial++) {
            finalFiles.push(this.files[initial])
        }
        updateFileNameDisplayArea()
    });

    document.getElementById(uploadButton).addEventListener("click", function(e) {
        var fileList = new DataTransfer()
        var fileNum = finalFiles.length;
        var initial = 0;
        for (initial; initial < fileNum; initial++) {
            fileList.items.add(finalFiles[initial])            
        }
        uploadFileList(fileList)
        
    })
	
})