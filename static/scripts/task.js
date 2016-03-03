/*

js file that handles the request and response for GET,POST

*/
$(function() {
    
    //OnLoad
    load_tasks();
    
    //Task-form on submit handler
    $('#task-form').on('submit', function(event){
        event.preventDefault(); //the default action will not be triggered ie. load_tasks
        create_task();
    });

    // AJAX for posting
    function create_task() {
        console.log("Creating a new Task")
        $.ajax({
            url : "api/tasks/",
            type : "POST", 
            data : { 
                title :  $('#task-title').val(),
                description : $('#task-description').val()
             }, 
            
            //Success or Error handling from GET response
            success : function(json) {

                console.log("Successfully created a new task : " + json);

                //clear out the input values
                $('#task-title').val(''); 
                $('#task-description').val(''); 

                //Append the new task onto the list -- to update it
                $("#talk").prepend("<li id='task-'><strong>"+json.title+"</strong>: <em> "+json.description+"</em>" );
            },

            error : function(xhr,errmsg,err) {
                error_message(xhr,errmsg,err);
            }
        });
    };

    // Load all tasks on page load
    function load_tasks() {
        $.ajax({
            url : "api/tasks/", 
            type : "GET", 
            
            //Success or Error handling from POST response
            success : function(json) {
                for (var i = 0; i < json.length; i++) {
                    $("#talk").prepend("<li id='task-"+i+"'><strong>"+json[i].title+"</strong>: <em> "+json[i].description+"</em>" );
                }
            },
            
            error : function(xhr,errmsg,err) {
                error_message(xhr,errmsg,err);
            }
        });
    };

    function error_message(xhr,errmsg,err){
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    };

});


