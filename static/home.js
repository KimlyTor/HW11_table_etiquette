$(document).ready(function(){
    $("#bsc-rul-btn").click(function(e){
        window.location.href = `http://127.0.0.1:5000/basic_rules/1`;
    });

    $("#tbl-set-btn").click(function(e){
        window.location.href = `http://127.0.0.1:5000/table_setting`;
    });

    $("#qz-btn").click(function(e){
        window.location.href = `http://127.0.0.1:5000/quiz`;
    });
});