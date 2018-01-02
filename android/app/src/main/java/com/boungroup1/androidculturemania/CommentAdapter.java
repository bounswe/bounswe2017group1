package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

import de.hdodenhof.circleimageview.CircleImageView;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 29/11/2017.
 */

public class CommentAdapter extends RecyclerView.Adapter<CommentAdapter.MyViewHolder>{

    private ArrayList<JsonResponseComment> heritageList;
    private Context mContext;


    /**
     * View Holder class for recyclerview
     */
    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView text, creator_username ;
        private CircleImageView comment_avatar;
        private Button comment_delete;

        /**
         * constructer for class
         * @param view parent view
         */
        public MyViewHolder(View view) {
            super(view);
            mContext = view.getContext();
            text = (TextView) view.findViewById(R.id.comment_text);
            creator_username = (TextView) view.findViewById(R.id.comment_creator);
            comment_avatar = (CircleImageView) view.findViewById(R.id.avatar_comment);
            comment_delete = (Button) view.findViewById(R.id.comment_delete);
            comment_delete.setVisibility(View.INVISIBLE);
        }
    }

    /**
     * constructor
     * @param context activity context
     * @param heritageList heritage list to be listed
     */
    public CommentAdapter(Context context,ArrayList<JsonResponseComment> heritageList) {
        this.mContext = context;
        this.heritageList = heritageList;
    }

    /**
     * interface method
     * @param parent parent view
     * @param viewType parent view type
     * @return custom view
     */
    @Override
    public CommentAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.comment_view, parent, false);

        return new CommentAdapter.MyViewHolder(itemView);
    }

    /**
     * method to run while binding
     * @param holder custom view holder
     * @param position position of the item
     */
    @Override
    public void onBindViewHolder(CommentAdapter.MyViewHolder holder, int position) {

        final JsonResponseComment heritageItem = heritageList.get(position);
        //Render image using Picasso library
        if (!TextUtils.isEmpty(heritageItem.getCreator_image_path())) {
            Log.d("IMAGE_PATH",ApiClient.BASE_URL+heritageItem.getCreator_image_path());
            Picasso.with(mContext).load(ApiClient.BASE_URL+heritageItem.getCreator_image_path())
                    .error(R.drawable.avatar)
                    .placeholder(R.drawable.avatar)
                    .into(holder.comment_avatar);
        }
        if(heritageItem.isIs_owner())
            holder.comment_delete.setVisibility(View.VISIBLE);
        holder.comment_delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                deleteComment(heritageItem.getId());
            }
        });
        holder.text.setText(heritageItem.getText());
        holder.creator_username.setText("By " + heritageItem.getCreator_username());
    }

    /**
     * delete comment function
     * @param id id of the comment
     */
    private void deleteComment(int id){
        Retrofit retrofit = ApiClient.getApiClient();
        final SharedPreferences sharedPref = mContext.getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseDeleteComment> call = apiInterface.deleteComment(id,"Token " + token);
        call.enqueue(new Callback<JsonResponseDeleteComment>() {
            @Override
            public void onResponse(Call<JsonResponseDeleteComment> call, Response<JsonResponseDeleteComment> response) {
                Toast.makeText(mContext.getApplicationContext(), "COMMENT DELETED", Toast.LENGTH_SHORT).show();
                ((ItemDetailView)mContext).getCommentList();
            }

            @Override
            public void onFailure(Call<JsonResponseDeleteComment> call, Throwable t) {
                Toast.makeText(mContext.getApplicationContext(), "COMMENT DELETED SUCCESSFULLY", Toast.LENGTH_SHORT).show();
                ((ItemDetailView)mContext).getCommentList();
            }
        });
    }


    /**
     * get the size of the list
     * @return size of the list
     */
    @Override
    public int getItemCount() {
        return heritageList.size();
    }

}
