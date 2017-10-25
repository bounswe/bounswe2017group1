package com.boungroup1.androidculturemania;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 24/10/2017.
 */

public class SingUpActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        final EditText email = (EditText) findViewById(R.id.input_email);
        final EditText username = (EditText) findViewById(R.id.input_name);
        final EditText password = (EditText) findViewById(R.id.input_password);
        final EditText gender = (EditText) findViewById(R.id.gender);
        final EditText location = (EditText) findViewById(R.id.location);

        Button btn_signUp = (Button) findViewById(R.id.btn_signup);

        btn_signUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email_str = email.getText().toString().trim();
                String username_str = username.getText().toString().trim();
                String password_str = password.getText().toString().trim();
//                String gender_str = gender.getText().toString();
//                String location_str = location.getText().toString();

                if(!TextUtils.isEmpty(email_str) && !TextUtils.isEmpty(username_str) && !TextUtils.isEmpty(password_str))
                {
                   // Toast.makeText(getApplicationContext(), "username: " + username_str + " email: "+ email_str + " password: " + password_str, Toast.LENGTH_SHORT).show();
                    sendPost(username_str, email_str, password_str);
                }
            }
        });

    }

    public void sendPost(String email, String username, String password){
        Retrofit retrofit = ApiClient.getApiClient();

        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseSignUp> call = apiInterface.signUp(new SignUpBody(username,  email, password));
        call.enqueue(new Callback<JsonResponseSignUp>() {
            @Override
            public void onResponse(Call<JsonResponseSignUp> call, Response<JsonResponseSignUp> response) {

                if (response.code() == 200) {
                        Toast.makeText(getApplicationContext(), "SUCCESS", Toast.LENGTH_SHORT).show();
                } else {

                   Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                   Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseSignUp> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
