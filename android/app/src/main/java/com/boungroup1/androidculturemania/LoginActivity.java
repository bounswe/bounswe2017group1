package com.boungroup1.androidculturemania;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by mustafa on 10/20/17.
 */

public class LoginActivity extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        final EditText username = (EditText) findViewById(R.id.input_username);
        final EditText email = (EditText) findViewById(R.id.input_email);
        final EditText password = (EditText) findViewById(R.id.input_password);
        final TextView link_signup = (TextView) findViewById(R.id.link_signup);

        Button btn_login = (Button) findViewById(R.id.btn_login);

        btn_login.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View view) {
                String email_str = email.getText().toString().trim();
                String username_str = username.getText().toString().trim();
                String password_str = password.getText().toString().trim();

                if(!TextUtils.isEmpty(email_str) && !TextUtils.isEmpty(username_str) && !TextUtils.isEmpty(password_str))
                {
                    // Toast.makeText(getApplicationContext(), "username: " + username_str + " email: "+ email_str + " password: " + password_str, Toast.LENGTH_SHORT).show();
                    sendPost(username_str, email_str, password_str);
                }

            }
        });


    }


    public void sendPost(String username,String email, String password){
        Retrofit retrofit = ApiClient.getApiClient();

        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseSignIn> call = apiInterface.signIn(new SignInBody(username,  email, password));
        call.enqueue(new Callback<JsonResponseSignIn>() {
            @Override
            public void onResponse(Call<JsonResponseSignIn> call, Response<JsonResponseSignIn> response) {

                if (response.isSuccessful()) {
                    Toast.makeText(getApplicationContext(), "SUCCESS", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                    Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseSignIn> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });
    }

}
