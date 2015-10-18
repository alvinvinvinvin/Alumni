$(document).ready(function() {
	$("#sign_in").click(function() {
		$("#register_block").hide();
		$("#login_block").fadeIn();
	});
});

function login_message(){
	$.post(location.protocol + '//' 
		  	+ location.host + "/ajax_signin/",
		  	{"account":document.getElementsByName("account")[0].value,
		  		"password":document.getElementsByName("password")[0].value,
		  		"type" : document.getElementsByName("type")[0].value},
		  	
		  	function(ret) {
		  		if(ret == '0'){
		  			alert("Invalid account or password. Please input again.");
		  		}else{
		  			alert("Sign in successfully!");
		  			location=location.protocol + '//'+ location.host;
		  		}
		  	});
}

// Regular Expression
var patrn_ACCOUNT = /\w{6,20}$/;
var patrn_PASSWORD = /\w{6,20}$/;
var patrn_NAME = /[a-zA-Z]{1,20}$/;
var patrn_EMAIL = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
var patrn_PHONE = /[1-9]\d{2}[1-9]\d{6}$/;
var patrn_ZIP = /\d{5}$/;
var patrn_DATE = /^(\d{4})[-\/](\d{2})$/;

function isValidDate(date)
{
    var matches = patrn_DATE.exec(date);
    if (matches == null) return false;
    var m = matches[2] - 1;
    var y = matches[1];
    var composedDate = new Date(y, m, 1);
    return composedDate.getMonth() == m &&
            composedDate.getFullYear() == y;
}


function ajax_register(){
	
	count = 0;
	
	if(!patrn_ACCOUNT.exec(document.getElementsByName("account")[0].value)){
		document.getElementsByName("message_account")[0].style.display = "inline";
		document.getElementsByName("message_account")[0].innerHTML = "Only characters, numbers or '_' are allowed; length: 6-20";
		count ++;
	}else{
		document.getElementsByName("message_account")[0].innerHTML = "";
	}
	
	if(!patrn_PASSWORD.exec(document.getElementsByName("password")[0].value)){
		document.getElementsByName("message_password")[0].style.display = "inline";
		document.getElementsByName("message_password")[0].innerHTML = "Only characters, numbers or '_' are allowed; length: 6-20";
		count ++;
	}else{
		document.getElementsByName("message_password")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("password_confirm")[0].value != document.getElementsByName("password")[0].value){
		document.getElementsByName("message_passwordconfirm")[0].style.display = "inline";
		document.getElementsByName("message_passwordconfirm")[0].innerHTML = "Password should match";
		count ++;
	}else{
		document.getElementsByName("message_passwordconfirm")[0].innerHTML = "";
	}

	if(!patrn_NAME.exec(document.getElementsByName("first_name")[0].value)){
		document.getElementsByName("message_first_name")[0].style.display = "inline";
		document.getElementsByName("message_first_name")[0].innerHTML = "Only characters; length: 6-20";
		count++;
	}else{
		document.getElementsByName("message_first_name")[0].innerHTML = "";
	}
	
	if(!patrn_NAME.exec(document.getElementsByName("last_name")[0].value)){
		document.getElementsByName("message_last_name")[0].style.display = "inline";
		document.getElementsByName("message_last_name")[0].innerHTML = "Only characters; length: 6-20";
		count++;
	}else{
		document.getElementsByName("message_last_name")[0].innerHTML = "";
	}
	
	if(!patrn_EMAIL.exec(document.getElementsByName("email")[0].value)){
		document.getElementsByName("message_email")[0].style.display = "inline";
		document.getElementsByName("message_email")[0].innerHTML = "The format of email is invalid";
		count++;
	}else{
		document.getElementsByName("message_email")[0].innerHTML = "";
	}
	
	var graduate_date = document.getElementsByName("graduate_date")[0].value;
	
	if(graduate_date ==""){
		document.getElementsByName("message_graduate_date")[0].style.display = "inline";
		document.getElementsByName("message_graduate_date")[0].innerHTML = "Please select your graduate date";		
		count++;
	}else if(!isValidDate(graduate_date)){
		document.getElementsByName("message_graduate_date")[0].style.display = "inline";
		document.getElementsByName("message_graduate_date")[0].innerHTML = "Invalid format, please use datepicker.";		
		count++;
	}else{
		/*
		 * graduate_year =
		 * document.getElementsByName("graduate_date")[0].value.split('-')[0];
		 * graduate_month =
		 * document.getElementsByName("graduate_date")[0].value.split('-')[1];
		 * if(new Date(graduate_year, graduate_month, "01").getTime() > new
		 * Date().getTime()){
		 * document.getElementsByName("message_graduate_date")[0].style.display =
		 * "inline";
		 * document.getElementsByName("message_graduate_date")[0].innerHTML =
		 * "Graduation date should be earlier than today"; count++; }else{
		 * document.getElementsByName("message_graduate_date")[0].innerHTML =
		 * ""; }
		 */
		document.getElementsByName("message_graduate_date")[0].innerHTML = "";
	}
	
	if(count == 0){
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_register/",
			  	{"account":document.getElementsByName("account")[0].value,
			  		"password":document.getElementsByName("password")[0].value,
			  		"password_confirm":document.getElementsByName("password_confirm")[0].value,
			  		"first_name":document.getElementsByName("first_name")[0].value,
			  		"last_name":document.getElementsByName("last_name")[0].value,
			  		"email":document.getElementsByName("email")[0].value,
			  		"graduate_date":document.getElementsByName("graduate_date")[0].value,
			  		"gender":document.getElementsByName("gender")[0].value},
			  	
			  	function(ret) {
			  		if(ret == '0'){

			  			alert("Your application has been processing.\n We will sent email to you if it gets approved.\n Thank you.");
			  			location=location.protocol + '//'+ location.host;
			  		}else if(ret == '1'){
			  			document.getElementsByName("message_account")[0].style.display = "inline";
			  			document.getElementsByName("message_account")[0].innerHTML = "Someone already has that username. Please try another one.";
			  			document.getElementsByName("message_email")[0].innerHTML = "";
			  		}else if(ret == '2'){
			  			document.getElementsByName("message_account")[0].innerHTML = "";
			  			document.getElementsByName("message_email")[0].style.display = "inline";
			  			document.getElementsByName("message_email")[0].innerHTML = "Someone already has that email.. Please try another one.";
			  		}else if(ret == '3'){
			  			document.getElementsByName("message_account")[0].style.display = "inline";
			  			document.getElementsByName("message_account")[0].innerHTML = "Someone already has that username. Please try another one.";
			  			document.getElementsByName("message_email")[0].style.display = "inline";
			  			document.getElementsByName("message_email")[0].innerHTML = "Someone already has that email.. Please try another one.";
			  		}else{
			  		}
			  	});
	}
}

function ajax_education(){
	count = 0;
	
	if(document.getElementsByName("major")[0].value == ""){
		document.getElementsByName("message_major")[0].style.display = "inline";
		document.getElementsByName("message_major")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_major")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("start_date")[0].value == ""){
		document.getElementsByName("message_start_date")[0].style.display = "inline";
		document.getElementsByName("message_start_date")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_start_date")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("end_date")[0].value == ""){
		document.getElementsByName("message_end_date")[0].style.display = "inline";
		document.getElementsByName("message_end_date")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_end_date")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("school")[0].value == ""){
		document.getElementsByName("message_school")[0].style.display = "inline";
		document.getElementsByName("message_school")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_school")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("address")[0].value == ""){
		document.getElementsByName("message_address")[0].style.display = "inline";
		document.getElementsByName("message_address")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_address")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("city")[0].value == ""){
		document.getElementsByName("message_city")[0].style.display = "inline";
		document.getElementsByName("message_city")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_city")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("state")[0].value == ""){
		document.getElementsByName("message_state")[0].style.display = "inline";
		document.getElementsByName("message_state")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_state")[0].innerHTML = "";
	}
	
	if(!patrn_ZIP.exec(document.getElementsByName("zip")[0].value)){
		document.getElementsByName("message_zip")[0].style.display = "inline";
		document.getElementsByName("message_zip")[0].innerHTML = "Invalid";
		count++;
	}else{
		document.getElementsByName("message_zip")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("description")[0].value == ""){
		document.getElementsByName("message_description")[0].style.display = "inline";
		document.getElementsByName("message_description")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_description")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("start_date")[0].value != "" && document.getElementsByName("end_date")[0].value != ""){
		graduate_year1 = document.getElementsByName("start_date")[0].value.split('-')[0];
		graduate_month1 = document.getElementsByName("start_date")[0].value.split('-')[1];
		
		graduate_year2 = document.getElementsByName("end_date")[0].value.split('-')[0];
		graduate_month2 = document.getElementsByName("end_date")[0].value.split('-')[1];
		
		if(new Date(graduate_year1, graduate_month1, "01").getTime() >= new Date(graduate_year2, graduate_month2, "01").getTime()){
			alert("Start date should be earlier than end date.\n" +
					"Please input again.")
			count++;
		}
	}
	
	if(count == 0){
		alert("Update successfully!");
		document.forms[0].submit();
	}
	
}

function ajax_working(){
	count = 0;
	
	if(document.getElementsByName("title")[0].value == ""){
		document.getElementsByName("message_title")[0].style.display = "inline";
		document.getElementsByName("message_title")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_title")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("start_date")[0].value == ""){
		document.getElementsByName("message_start_date")[0].style.display = "inline";
		document.getElementsByName("message_start_date")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_start_date")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("end_date")[0].value == ""){
		document.getElementsByName("message_end_date")[0].style.display = "inline";
		document.getElementsByName("message_end_date")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_end_date")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("company")[0].value == ""){
		document.getElementsByName("message_company")[0].style.display = "inline";
		document.getElementsByName("message_company")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_company")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("address")[0].value == ""){
		document.getElementsByName("message_address")[0].style.display = "inline";
		document.getElementsByName("message_address")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_address")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("city")[0].value == ""){
		document.getElementsByName("message_city")[0].style.display = "inline";
		document.getElementsByName("message_city")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_city")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("state")[0].value == ""){
		document.getElementsByName("message_state")[0].style.display = "inline";
		document.getElementsByName("message_state")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_state")[0].innerHTML = "";
	}
	
	if(!patrn_ZIP.exec(document.getElementsByName("zip")[0].value)){
		document.getElementsByName("message_zip")[0].style.display = "inline";
		document.getElementsByName("message_zip")[0].innerHTML = "Invalid";
		count++;
	}else{
		document.getElementsByName("message_zip")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("description")[0].value == ""){
		document.getElementsByName("message_description")[0].style.display = "inline";
		document.getElementsByName("message_description")[0].innerHTML = "Require";
		count ++;
	}else{
		document.getElementsByName("message_description")[0].innerHTML = "";
	}
	
	if(document.getElementsByName("start_date")[0].value != "" && document.getElementsByName("end_date")[0].value != ""){
		graduate_year1 = document.getElementsByName("start_date")[0].value.split('-')[0];
		graduate_month1 = document.getElementsByName("start_date")[0].value.split('-')[1];
		
		graduate_year2 = document.getElementsByName("end_date")[0].value.split('-')[0];
		graduate_month2 = document.getElementsByName("end_date")[0].value.split('-')[1];
		
		if(new Date(graduate_year1, graduate_month1, "01").getTime() >= new Date(graduate_year2, graduate_month2, "01").getTime()){
			alert("Start date should be earlier than end date.\n" +
					"Please input again.")
			count++;
		}
	}
	
	if(count == 0){
		alert("Update successfully!");
		document.forms[0].submit();
	}
	
}

function ajax_addgroup(){
	if(document.getElementsByName("groupname")[0].value == ""){
		alert("Group name can't be blank!");
	}else{
		$("#addgroup").submit();
	}
		
}

function ajax_admin_account_add(){
	count = 0;
	var account = document.getElementsByName("account")[0].value;
	var message_account = document.getElementsByName("message_account")[0];
	var passwordone = document.getElementsByName("passwordone")[0].value;
	var message_passwordone = document.getElementsByName("message_passwordone")[0];
	var passwordtwo = document.getElementsByName("passwordtwo")[0].value;
	var message_passwordtwo = document.getElementsByName("message_passwordtwo")[0];
	var first_name = document.getElementsByName("first_name")[0].value;
	var message_first_name = document.getElementsByName("message_first_name")[0];
	var last_name = document.getElementsByName("last_name")[0].value;
	var message_last_name = document.getElementsByName("message_last_name")[0];
	
	if(account == ""){
		message_account.style.display = "inline";
		message_account.innerHTML = "Required";
		count ++;
	}else{
		message_account.innerHTML = "";
	}
	
	if(passwordone == ""){
		message_passwordone.style.display = "inline";
		message_passwordone.innerHTML = "Required";
		count ++;
	}else{
		message_passwordone.innerHTML = "";
	}
	
	if(passwordtwo != passwordone){
		message_passwordtwo.style.display = "inline";
		message_passwordtwo.innerHTML = "Different!";
		count ++;
	}else{
		message_passwordtwo.innerHTML = "";
	}
	
	
	if(first_name == ""){
		message_first_name.style.display = "inline";
		message_first_name.innerHTML = "Required";
		count ++;
	}else{
		message_first_name.innerHTML = "";
	}
	
	if(last_name == ""){
		message_last_name.style.display = "inline";
		message_last_name.innerHTML = "Required";
		count ++;
	}else{
		message_last_name.innerHTML = "";
	}
	
	if(count == 0){
		document.forms[0].submit();
	}
	
}

function ajax_get_radio_update(){
	var account = $('input[name="radio"]:checked').val();
	
	if(account == null ){
		alert('please select one account first.');
		return;
	}
	else{
		location = location.protocol + '//' 
	  	+ location.host + "/admin_account_update/?account="+account;
	}
}

function ajax_admin_account_update(){
	count = 0;
	var account = getUrlParameter("account");
	var message_account = document.getElementsByName("message_account")[0];
	var passwordone = document.getElementsByName("passwordone")[0].value;
	var message_passwordone = document.getElementsByName("message_passwordone")[0];
	var passwordtwo = document.getElementsByName("passwordtwo")[0].value;
	var message_passwordtwo = document.getElementsByName("message_passwordtwo")[0];
	var first_name = document.getElementsByName("first_name")[0].value;
	var message_first_name = document.getElementsByName("message_first_name")[0];
	var last_name = document.getElementsByName("last_name")[0].value;
	var message_last_name = document.getElementsByName("message_last_name")[0];

	
	if(passwordone == ""){
		message_passwordone.style.display = "inline";
		message_passwordone.innerHTML = "Required";
		count ++;
	}else{
		message_passwordone.innerHTML = "";
	}
	
	if(passwordtwo != passwordone){
		message_passwordtwo.style.display = "inline";
		message_passwordtwo.innerHTML = "Different!";
		count ++;
	}else{
		message_passwordtwo.innerHTML = "";
	}
	
	
	if(first_name == ""){
		message_first_name.style.display = "inline";
		message_first_name.innerHTML = "Required";
		count ++;
	}else{
		message_first_name.innerHTML = "";
	}
	
	if(last_name == ""){
		message_last_name.style.display = "inline";
		message_last_name.innerHTML = "Required";
		count ++;
	}else{
		message_last_name.innerHTML = "";
	}
	
	if(count == 0){
		$.post(location.protocol+'//'+location.host+"/admin_account_update/",
				{"account":account,
			"passwordone":passwordone,
			"first_name":first_name,
			"last_name":last_name,},
			
			function(ret){
				if(ret == 1){
					alert("Updating successfully.");
					location = location.protocol+'//'+location.host + "/admin_account/";
				}
				else{
					alert("Someting wrong happened during updating, please contact with administrator.");
				}
			}
		);
//		document.forms[0].submit();
	}
	
}

function ajax_get_radio_delete(){
var account = $('input[name="radio"]:checked').val();
	
	if(account == null ){
		alert('please select one account first.');
		return;
	}
	else{
		var confirmation = confirm("Are you sure you want to delete account: "+account+" ?")
		if(confirmation == true){
			$.post(location.protocol + '//' 
				  	+ location.host + "/admin_account_delete/",
				  	{"account":account},
				  	
				  	function(ret){
				  		if(ret == 1){
				  			alert("Deleting successfully.");
				  			location = location.protocol + '//' 
						  	+ location.host + "/admin_account/";
				  		}
				  		else{
				  			alert("Deleting failed, someting wrong happened, please contact your administrator.");
				  			return;
				  		}
				  	});
		}
		else{
			return;
		}
	}
}

function getUrlParameter(sParam) {

	var sPageURL = window.location.search.substring(1);
	console.log(sPageURL);
	var sURLVariables = sPageURL.split('&');

	for (var i = 0; i < sURLVariables.length; i++) {

		var sParameterName = sURLVariables[i].split('=');

		if (sParameterName[0] == sParam) {

			return sParameterName[1];

		}
	}
}