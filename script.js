var company_id=["amazon","ebay","walmart"];
var isPaused = true;


var check = function(){
    if(isPaused){
        setTimeout(check, 1000); 
    }
}

function search(){
	practice(0)
}

//0 - search
function practice(mode){
	//search_from 0 = Amazon, 1 = Ebay, 2 = Walmart
	var search_key = document.getElementById("search_input").value;
	var search_from;
	var string_to_send;
	var recieved_data;
	

	for (var i = 0; i < company_id.length; i++){
		company = company_id[i];
		if (document.getElementById(company).classList.contains("active")){
			search_from = company;
		}


	}

	//window.alert("keyword is "+search_key);
	//window.alert("searching from "+search_from);
	if (mode==0){
		string_to_send=search_key+","+search_from+",0";
	}
	if (mode==1){
		string_to_send=search_key+","+search_from+",1";
	}
	
	/*
	var text = search_key+","+search_from;
	var bad = "EVAL" + JSON.stringify(text)+" 0\r\n";
	var x = new XMLHttpRequest();
	x.open("POST", "http://localhost:8000");
	x.send(bad);
	window.alert(x.responseText);
*/
	socket = new WebSocket('ws://127.0.0.1:8080');
	socket.onopen= function() {
		//window.alert(string_to_send)
    	socket.send(string_to_send);
	};
	socket.onmessage= function(s) {
    	//window.alert('got reply '+s.data);
    	//document.getElementById('table').innerHTML = JSON.stringify(s.data);
    	//recieved_data=s.data;
    	
    	
    	amazon_score=s.data[s.data.length-3];
    	ebay_score=s.data[s.data.length-2];
    	walmart_score=s.data[s.data.length-1];
    	
    	doSomething(s.data.slice(0,s.data.length-3));
    	doSomething1(amazon_score);
    	doSomething2(ebay_score);
    	doSomething3(walmart_score);
    	while(isPaused){
    		check();
    	}
    	socket.close();
    	
	};


	
	
}

function doSomething(data){
	document.getElementById('table').innerHTML = data;
	isPaused=false;
}

function doSomething1(data){
	document.getElementById('amazon_score').innerHTML = data;
	isPaused=false;
}

function doSomething2(data){
	document.getElementById('ebay_score').innerHTML = data;
	isPaused=false;
}

function doSomething3(data){
	document.getElementById('walmart_score').innerHTML = data;
	isPaused=false;
}

function change_search_from(current){
	
	company_id.forEach(removeClass);
	//window.alert(current);
	document.getElementById(current).classList.add("active");
	company_id.forEach(printClass);
	practice(1)
}
function removeClass(company){
	document.getElementById(company).classList.remove("active");
}
function printClass(company){
	if (document.getElementById(company).classList.contains("active")){
		//window.alert(company);
	}
			
}


function hamburger_menu_function(x) {
  x.classList.toggle("change");
}

function check_login_form(){
	/*checking if  email was entered correctly*/
	/*email with form something@something.something*/
	/*the character before @ can not have <>{}[]...*/
	var email = document.forms["login_user"]["user_email_login"].value;
	if(email == ''||!(isValidEmail(email))){
		window.alert("please re-enter email address");
		document.login_user.user_email_login.focus();
		return false;
	}
	var password = document.forms["login_user"]["user_password_login"].value;
	if (password == '' || (password.length < 7)){
		window.alert("Please re-enter password");
		document.login_user.user_password_login.focus();
		return false;
	}
}

function check_register_form(){
	/*checking the name input is longer that 3 letters, shorter than 30 letters, and only contains alphabets */
	var username = document.forms["register_new_user"]["user_name"].value;
	if(username == ''||!(username.length >=3 && username.length <=30 && /^[a-zA-Z ]*$/.test(username))){
		window.alert("please enter a valid name");
		document.register_new_user.user_name.focus();
		return false;
	}
	/*checking if birth date was entered correctly*/
	var bd = document.forms["register_new_user"]["user_bdate"].value;
	if(bd == ''||!(isValidDate(bd))){
		window.alert("please enter a valid birth date");
		document.register_new_user.user_bdate.focus();
		return false;
	}
	/*checking if  email was entered correctly*/
	/*email with form something@something.something*/
	/*the character before @ can not have <>{}[]...*/
	var email = document.forms["register_new_user"]["user_email"].value;
	if(email == ''||!(isValidEmail(email))){
		window.alert("please enter a valid email address");
		document.register_new_user.user_email.focus();
		return false;
	}
	/*checking if password is in correct format.*/
	var password = document.forms["register_new_user"]["user_password"].value;
	var password_re = document.forms["register_new_user"]["user_password_re"].value;
	if(password != password_re){
		window.alert("password does not match!");
		document.register_new_user.user_password.value = '';
		document.register_new_user.user_password_re.value = '';
		document.register_new_user.user_password.focus();
		return false;
	}
	if(password==''){
		window.alert("Please enter password");
		document.register_new_user.user_password.value = '';
		document.register_new_user.user_password_re.value = '';
		document.register_new_user.user_password.focus();
	}

	/*checking if phone number was entered correctly*/
	/*10 digit number with/without dash*/
	var pnumber = document.forms["register_new_user"]["user_phonenumber"].value;
	if(pnumber == ''||!(/^([0-9]{3}-[0-9]{3}-[0-9]{4})|([0-9]{3}[0-9]{3}[0-9]{4})$/.test(pnumber))){
		window.alert("please enter a valid phone number");
		document.register_new_user.user_phonenumber.focus();
		return false;
	}
	/*checking if card number was entered correctly*/
	/*16 digit number with/without space*/
	var cardnumber = document.forms["register_new_user"]["user_card_number"].value;
	if(cardnumber == ''||!(/^([0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4})|([0-9]{16})$/.test(cardnumber))){
		window.alert("please enter a valid card number");
		document.register_new_user.user_card_number.focus();
		return false;
	}

	/*checking if expirary date was entered correctly*/
	var expireDate = document.forms["register_new_user"]["user_card_date"].value;
	if(expireDate == ''||!(isValidDate1(expireDate))){
		window.alert("please enter a valid expirary date");
		document.register_new_user.user_card_date.focus();
		return false;
	}
	/*checking if cvv was entered correctly*/
	var cvv = document.forms["register_new_user"]["user_card_cvv"].value;
	if(cvv == ''||!(/^([0-9]{3})$/.test(cvv))){
		window.alert("please enter a valid cvv");
		document.register_new_user.user_card_cvv.focus();
		return false;
	}
	/*checking if address was entered correctly*/
	var cardAddress = document.forms["register_new_user"]["user_card_address"].value;
	if(cardAddress == ''||isValidAddress(cardAddress)){
		window.alert("please enter a valid address");
		document.register_new_user.user_card_address.focus();
		return false;
	}


}

/*checking for valid address using google geocoder*/
function isValidAddress(address){
	geocoder = new google.maps.Geocoder();
	geocoder.geocode({ 'address': address}, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                return false;
            } else {               
                return true;
            }
          });
}


/*checking for valid email address*/
function isValidEmail(email){
	/*the part befor @ can't have <>()....*/
	/*and the email need to have format of something@somthing.somthing*/
  	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})$/;
  	return re.test(email);
}

/*checking whether date given is valid*/
function isValidDate(bd){
	/*checking if the format is corret*/
	/*format of YYYY-MM(M)-DD(M) is accepted*/
	if(!/^\d{4}\-\d{1,2}\-\d{1,2}$/.test(bd)){
        return false;
	}

    // divide the input into year, month and date to validate
    var split_input = bd.split("-");
    var year = parseInt(split_input[0], 10);
    var month = parseInt(split_input[1], 10);
    var day = parseInt(split_input[2], 10);
    
    

    // since it is birthdate, year range is set from 1918 to 2018
    if(year <= 1919 || year > 2019 || month == 0 || month > 12)
        return false;
    /*checks for if day provided is in range*/
    var daysInMonth = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

    if(day<=0 || day>daysInMonth[month-1])
    	return false;

    if (!isExpired(year,month,day)){
		return false;
	}

    return true;
}

/*checking whether date given is valid*/
function isValidDate1(bd){
	/*checking if the format is corret*/
	/*format of YYYY-MM(M)-DD(M) is accepted*/
	if(!/^\d{4}\-\d{1,2}\-\d{1,2}$/.test(bd)){
        return false;
	}

    // divide the input into year, month and date to validate
    var split_input = bd.split("-");
    var year = parseInt(split_input[0], 10);
    var month = parseInt(split_input[1], 10);
    var day = parseInt(split_input[2], 10);
    
    

    // since it is expire date, user can still enter credit card that is expired
    if(month == 0 || month > 12)
        return false;
    /*checks for if day provided is in range*/
    var daysInMonth = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

    if(day<=0 || day>daysInMonth[month-1])
    	return false;

    

	if (isExpired(year,month,day)){
		return false;
	}

    return true;
}

function isExpired(year, month, day){
	var today = new Date();
	var dd = String(today.getDate()).padStart(2, '0');
	var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
	var yyyy = today.getFullYear();

	var year=parseInt(year);
	var month=parseInt(month);
	var day=parseInt(day);

	if (year<yyyy){
		return true;
	}else if (year==yyyy){
		if (month<mm){
			return true;
		}else if (month==mm){
			if (day<dd){
				return true;
			}
		}
	}


	return false;

}

//password input thingys
