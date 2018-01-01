package com.boungroup1.androidculturemania;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

import de.hdodenhof.circleimageview.CircleImageView;

/**
 * Created by user on 29/11/2017.
 */

public class CommentAdapter extends RecyclerView.Adapter<CommentAdapter.MyViewHolder>{

    private ArrayList<JsonResponseComment> heritageList;
    private Context mContext;



    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView text, creator_username ;
        private CircleImageView comment_avatar;

        public MyViewHolder(View view) {
            super(view);
            text = (TextView) view.findViewById(R.id.comment_text);
            creator_username = (TextView) view.findViewById(R.id.comment_creator);
            comment_avatar = (CircleImageView) view.findViewById(R.id.avatar_comment);
        }
    }


    public CommentAdapter(Context context,ArrayList<JsonResponseComment> heritageList) {
        this.mContext = context;
        this.heritageList = heritageList;
    }

    @Override
    public CommentAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.comment_view, parent, false);

        return new CommentAdapter.MyViewHolder(itemView);
    }


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

        holder.text.setText(heritageItem.getText());
        holder.creator_username.setText("By " + heritageItem.getCreator_username());
    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }

}
