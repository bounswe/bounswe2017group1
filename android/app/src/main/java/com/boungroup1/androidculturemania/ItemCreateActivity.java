package com.boungroup1.androidculturemania;

import android.app.DatePickerDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.os.ParcelFileDescriptor;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.FileDescriptor;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Locale;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

//import static android.R.attr.password;
//import static com.boungroup1.androidculturemania.R.id.username;

/**
 * Created by user on 15/11/2017.
 */

public class ItemCreateActivity extends AppCompatActivity{
    int dateyear, datemonth, dateday;
    Uri imageUri = null;
    String videoUrl = null;



    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item_create);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        final EditText title = (EditText) findViewById(R.id.input_title);
        final EditText description = (EditText) findViewById(R.id.input_description);
        final EditText location = (EditText) findViewById(R.id.input_location);
        final EditText tags = (EditText) findViewById(R.id.tags);
        final Button btn_create_item = (Button) findViewById(R.id.btn_create_item);
        final EditText dateedit = (EditText) findViewById(R.id.date);
        final Button uploadImage = (Button) findViewById(R.id.uploadImage);

        uploadImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.setType("image/*");
                startActivityForResult(intent, 42);
            }
        });

        final Calendar myCalendar = Calendar.getInstance();

        final DatePickerDialog.OnDateSetListener date = new DatePickerDialog.OnDateSetListener() {

            @Override
            public void onDateSet(DatePicker view, int year, int monthOfYear,
                                  int dayOfMonth) {
                // TODO Auto-generated method stub
                dateyear = year;
                datemonth = monthOfYear;
                dateday = dayOfMonth;
                myCalendar.set(Calendar.YEAR, year);
                myCalendar.set(Calendar.MONTH, monthOfYear);
                myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                String myFormat = "MM/dd/yy"; //In which you need put here
                SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);

                dateedit.setText(sdf.format(myCalendar.getTime()));
            }

        };

        dateedit.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                new DatePickerDialog(ItemCreateActivity.this, date, myCalendar
                        .get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                        myCalendar.get(Calendar.DAY_OF_MONTH)).show();
            }
        });

        btn_create_item.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String title_str = title.getText().toString().trim();
                String description_str = description.getText().toString().trim();
                String location_str = location.getText().toString().trim();
                String tag_string = tags.getText().toString().trim();

                if (!TextUtils.isEmpty(title_str) && !TextUtils.isEmpty(description_str) && !TextUtils.isEmpty(location_str) && !TextUtils.isEmpty(tag_string))
                {
                    sendPost(title_str, description_str, location_str, tag_string);
                }
            }
        });

    }


    public void sendPost(final String title, final String description, final String location, final String tag){
        Retrofit retrofit = ApiClient.getApiClient();
        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        String[] tagstr = tag.split(",");
        List<Tag> tagsArray = new ArrayList<Tag>();
        for (String tagss : tagstr)
            tagsArray.add(new Tag(tagss, "cat"));
        EditText video_url_edit = (EditText) findViewById(R.id.video_url);
        videoUrl = video_url_edit.getText().toString();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseItemCreate> call = apiInterface.itemCreate(new ItemCreateBody(title, description, dateyear + "-"+ datemonth+"-"+dateday+" 06:00:00.000000",
                location,tagsArray ),"Token " + token);
        call.enqueue(new Callback<JsonResponseItemCreate>() {
            @Override
            public void onResponse(Call<JsonResponseItemCreate> call, Response<JsonResponseItemCreate> response) {

                if (response.isSuccessful()) {

                    int heritageId = response.body().getId();
                    if(imageUri!=null){
                        uploadImage(heritageId);
                    }
                    if(videoUrl!=null){
                        //uploadVideo(heritageId);
                    }


                    Log.d("deneme",response.body().getId().toString());

                    Toast.makeText(getApplicationContext(), "SUCCESS", Toast.LENGTH_SHORT).show();
//                    Log.d("RESPONSE", response.body().getProfile().getGender());
//                    openMain(response.body().getToken(), response.body().getProfile().getUsername(),
//                            response.body().getUser().getEmail(),
//                            response.body().getProfile().getId());
                    finish();
                    startActivity(new Intent(getApplicationContext(), MainActivity.class));
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                    Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseItemCreate> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });
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

    @Override
    public void onActivityResult(int requestCode, int resultCode,
                                 Intent resultData) {
        if(resultData!=null)
            imageUri = resultData.getData();
    }

    private void uploadImage(int heritageId){
        if(imageUri==null)
            return;
        if(videoUrl==null)
            return;
        final byte[] file = getBitmapFromUri(imageUri);
        String url = imageUri.toString();

        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        MultipartBody.Part filePart = MultipartBody.Part.createFormData("image", url.substring( url.lastIndexOf('/')+1, url.length() ), RequestBody.create(MediaType.parse("image/*"),file));
        Call<JsonResponseMedia> call = apiInterface.uploadImage("Token " + token,filePart, videoUrl , "image",heritageId,sdf.format(cal.getTime()),sdf.format(cal.getTime()));
        call.enqueue(new Callback<JsonResponseMedia>() {
            @Override
            public void onResponse(Call<JsonResponseMedia> call, Response<JsonResponseMedia> response) {
                Toast.makeText(getApplicationContext(),"Image successfully uploaded.",Toast.LENGTH_SHORT);
            }

            @Override
            public void onFailure(Call<JsonResponseMedia> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"Uploading image failed, try again.",Toast.LENGTH_SHORT);
            }
        });

    }

    private void uploadVideo(int heritageId){
        if(videoUrl==null)
            return;

        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        Call<JsonResponseMedia> call = apiInterface.uploadVideo("Token " + token,videoUrl,"video",heritageId,sdf.format(cal.getTime()),sdf.format(cal.getTime()));
        call.enqueue(new Callback<JsonResponseMedia>() {
            @Override
            public void onResponse(Call<JsonResponseMedia> call, Response<JsonResponseMedia> response) {
                Toast.makeText(getApplicationContext(),"Video successfully uploaded.",Toast.LENGTH_SHORT);
            }

            @Override
            public void onFailure(Call<JsonResponseMedia> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"Uploading image failed, try again.",Toast.LENGTH_SHORT);
            }
        });

    }

    private byte[] getBitmapFromUri(Uri uri) {
        byte[] byteArray = null;
        try{
            ParcelFileDescriptor parcelFileDescriptor =
                    getContentResolver().openFileDescriptor(uri, "r");
            FileDescriptor fileDescriptor = parcelFileDescriptor.getFileDescriptor();
            Bitmap image = BitmapFactory.decodeFileDescriptor(fileDescriptor);
            parcelFileDescriptor.close();
            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            image.compress(Bitmap.CompressFormat.PNG, 100, stream);
            byteArray = stream.toByteArray();
        }catch (IOException e){
        }
        return byteArray;
    }



}
