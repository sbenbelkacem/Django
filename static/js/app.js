(function () {
    $(document).ready(function () {
        $("#mon-profil").click(function () {
            var info = $("#information_profil");
            if (info.hasClass("hidden"))
                info.removeClass("hidden");
            else info.addClass("hidden");
        });

        $('#discard').keypress(function (e) {
            var key = e.which;
            if (key == 13)  // the enter key code
            {
                console.log("discard pressed");
                return false;
            }
        })
        $('#save-email').keypress(function (e) {
            var key = e.which;
            if (key == 13)  // the enter key code
            {
                saveEmail();
            }

        })


        $("#save-email").click(function () {
            saveEmail();
        });

        function saveEmail() {
            $('#myModal').modal('hide');

            var email = $('#email').val();
            var profile_id = $('#profile_id').val();

            $.ajax({
                method: "POST",
                url: "/profil/update_email",
                data: {
                    id: profile_id,
                    email: email,
                },
                success: function (response) {
                    $("#addresse-email").text(response.email);
                },
            });
        }


        $(".nav-stacked li a ").click(function () {
            console.log($(this).closest("nav-stacked").find(".nav-stacked li a"));
            $(this).closest("ul").find("li a .active2").removeClass("active2");


            $(this).toggleClass("active2");

        });
    });


} ()); 