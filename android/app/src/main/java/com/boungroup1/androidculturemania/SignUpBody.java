package com.boungroup1.androidculturemania;

/**
 * Created by user on 24/10/2017.
 */

public class SignUpBody {
    public String username;
    public String email;
    public String password;
    public String location;
    public String gender;
    public String photo_path;


    public SignUpBody(String username, String email, String password, String location, String gender, String photo_path) {
        this.username = username;
        this.email = email;
        this.password = password;
        this.location = location;
        this.gender = gender;
        this.photo_path = photo_path;
    }
}
