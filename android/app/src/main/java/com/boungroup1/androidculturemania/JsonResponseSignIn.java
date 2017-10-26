package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by mustafa on 10/25/17.
 */

public class JsonResponseSignIn {
    @SerializedName("token")
    @Expose
    private String token;

    public JsonResponseSignIn(String token) {
        this.token = token;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
