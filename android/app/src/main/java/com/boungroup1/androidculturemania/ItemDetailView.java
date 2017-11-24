package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.text.method.ScrollingMovementMethod;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 22/11/2017.
 */

public class ItemDetailView extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.item_detail_view);

        final RelativeLayout layout = (RelativeLayout) findViewById(R.id.detail_view_relayout);
        layout.setVisibility(View.INVISIBLE);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();
        int heritageId = intent.getIntExtra("heritageId", -1);

        final TextView title = (TextView) findViewById(R.id.detailtitle);
        final TextView date = (TextView) findViewById(R.id.detaildate);
        final TextView location = (TextView) findViewById(R.id.detaillocation);
        final TextView name = (TextView) findViewById(R.id.detailname);
        final TextView description = (TextView) findViewById(R.id.detaildescription);
        ImageView image = (ImageView) findViewById(R.id.detailimage);

        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);

        Call<JsonResponseItemDetail> call = apiInterface.getItem(heritageId, "Token " + token);
        call.enqueue(new Callback<JsonResponseItemDetail>() {
            @Override
            public void onResponse(Call<JsonResponseItemDetail> call, Response<JsonResponseItemDetail> response) {
                if(response.isSuccessful())
                {
                    title.setText(response.body().getTitle());
                    date.setText(response.body().getCreation_date().toString());
                    location.setText(response.body().getLocation());
                    name.setText("By "+response.body().getCreator_username());
                    description.setText(response.body().getDescription());
                    layout.setVisibility(View.VISIBLE);
                }
            }

            @Override
            public void onFailure(Call<JsonResponseItemDetail> call, Throwable t) {

            }
        });

//        title.setText("TITLE");
//        date.setText("DATE");
//        location.setText("LOCATION");
//        name.setText("USERNAME");
//        description.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id scelerisque leo, in pharetra leo. Duis porta, urna sit amet convallis hendrerit, mi nulla gravida purus, ac facilisis velit felis eu elit. Fusce ornare neque massa, a cursus odio dapibus ut. Fusce pretium nisl a nibh varius, vel malesuada orci interdum. Aliquam erat volutpat. Aliquam erat volutpat. Morbi scelerisque ac massa sit amet eleifend. Vivamus venenatis erat et velit ultricies, eu rutrum nunc scelerisque. Cras elementum pharetra dui quis dictum. Nunc lacus nisi, blandit sed nunc non, lacinia gravida est. Aliquam pretium ultricies porttitor. Nunc fringilla mollis lacus non pulvinar. Sed bibendum augue eget lacus pellentesque auctor. Nunc id augue vitae eros interdum sodales. Mauris ullamcorper pellentesque pretium." +
//                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id scelerisque leo, in pharetra leo. Duis porta, urna sit amet convallis hendrerit, mi nulla gravida purus, ac facilisis velit felis eu elit. Fusce ornare neque massa, a cursus odio dapibus ut. Fusce pretium nisl a nibh varius, vel malesuada orci interdum. Aliquam erat volutpat. Aliquam erat volutpat. Morbi scelerisque ac massa sit amet eleifend. Vivamus venenatis erat et velit ultricies, eu rutrum nunc scelerisque. Cras elementum pharetra dui quis dictum. Nunc lacus nisi, blandit sed nunc non, lacinia gravida est. Aliquam pretium ultricies porttitor. Nunc fringilla mollis lacus non pulvinar. Sed bibendum augue eget lacus pellentesque auctor. Nunc id augue vitae eros interdum sodales. Mauris ullamcorper pellentesque pretium.");
        description.setMovementMethod(new ScrollingMovementMethod());




    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        finish();
        startActivity(new Intent(getApplicationContext(), MainActivity.class));
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            // Respond to the action bar's Up/Home button
            case android.R.id.home:
                finish();
                startActivity(new Intent(getApplicationContext(), MainActivity.class));
        }
        return super.onOptionsItemSelected(item);
    }
}
