package com.boungroup1.androidculturemania;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by user on 24/10/2017.
 */

public class ApiClient {
    public static final String BASE_URL = "http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com";
    public static Retrofit retrofit = null;

    public static Retrofit getApiClient(){
        if (retrofit == null){
            retrofit = new Retrofit.Builder().baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create()).build();
        }
        return retrofit;
    }
}
