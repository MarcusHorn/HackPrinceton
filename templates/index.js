$(document).ready(function(){
    // Time in milliseconds
    var timeDelay = 5000;
    // Folder location of the photos
    var folderName = 'Images'

    // Number of photos included
    var photos = 11;

    var prevIndex = 1;

    var curIndex = 1;

    var transition = function(){
        while (curIndex == prevIndex){
            curIndex = Math.floor(Math.random() * photos) + 1;
        }

        var photo = folderName + '/background' + curIndex + '.jpeg';

        document.body.background=photo;
        prevIndex = curIndex;

        //console.log(curIndex, prevIndex)
        
        setTimeout(transition, timeDelay);
    };

    var run = function(){
        var photo = folderName + '/background' + prevIndex + '.jpeg';

        document.body.background=photo;

        setTimeout(transition, timeDelay);
    };

    run();
})