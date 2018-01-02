package com.boungroup1.androidculturemania;

import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by mehmetsefa on 24/10/2017.
 * API client for creating Retrofit instance and returning the api client
 */

public class ApiClient {
    public static final String BASE_URL = "http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com:3000";
    public static Retrofit retrofit = null;

    /**
     * handles preparing retrofit client
     * @return retrofit client instance
     */
    public static Retrofit getApiClient(){
        if (retrofit == null){
            HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
            logging.setLevel(HttpLoggingInterceptor.Level.BODY);
            OkHttpClient client = new OkHttpClient.Builder().addInterceptor(logging).build();
            retrofit = new Retrofit.Builder().baseUrl(BASE_URL)
                    .client(client)
                    .addConverterFactory(GsonConverterFactory.create()).build();
        }
        return retrofit;
    }
}
