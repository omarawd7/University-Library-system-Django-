function checkForm() {
    var first = document.getElementById("first").value;
    var last = document.getElementById("last").value;
    var p1 = document.getElementById("p1").value;
    var p2 = document.getElementById("p2").value;
    var email = document.getElementById("email").value;


    if (first == "") {
        alert("Error: first name cannot be blank!");
        document.getElementById("first").focus();
        return false;
    }

    if (last == "") {
        alert("Error: last name cannot be blank!");
        document.getElementById("last").focus();
        return false;
    }



    if (p1 != "" && p1 == p2) {
        if (p1.length < 6) {
            alert("Error: Password must contain at least six characters!");
            document.getElementById("p1").focus();
            return false;
        }
        if (p1 == first) {
            alert("Error: Password must be different from first name!");
            document.getElementById("p1").focus();
            return false;
        }
        if (p1 == last) {
            alert("Error: Password must be different from last name!");
            document.getElementById("p1").focus();
            return false;
        }
        re = /[0-9]/;
        if (!re.test(p1)) {
            alert("Error: password must contain at least one number (0-9)!");
            document.getElementById("p1").focus();
            return false;
        }
        re = /[a-z]/;
        if (!re.test(p1)) {
            alert("Error: password must contain at least one character (a-z)!");
            document.getElementById("p1").focus();
            return false;
        }
        if (email == "") {
            alert("Error: Email cannot be blank!");
            document.getElementById("email").focus();
            return false;
        }
        
    } else {
        alert("Error: Please check that you've entered and confirmed your password!");
        document.getElementById("p1").focus();
        return false;
    }

    alert("Successfully Sign Up ♥ thanx "+first);
    
    return true;
    
}
