function check()
{
var username =document.getElementById("username").value;
var password =document.getElementById("pass").value;
var link= document.getElementById("link").value;
if(username=="")
{
    alert("Error:Please Enter The Username!")
    document.getElementById("username").focus();
    return false;
}

if(password=="")
{
    alert("Error:Please Enter The Password!")
    document.getElementById("password").focus();
    return false;
}
if(username==""&& password=="") 
{
    alert("Error:Please Enter The Username And Password!")
    document.getElementById("username").focus();
    document.getElementById("pass").focus();
    return false;
}

return true;
}
