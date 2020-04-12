package com.software.domain;

import java.util.ArrayList;

public class News {
    private String museumName;

    private String evaluation;

    private String source;

    private int newsId;

    private String newsTitle;

    private ArrayList<String> newsContent;

    public News(){}

    public String getMuseumName() {
        return museumName;
    }

    public String getEvaluation() {
        return evaluation;
    }

    public String getSource() {
        return source;
    }

    public int getNewsId() {
        return newsId;
    }

    public String getNewsTitle() {
        return newsTitle;
    }

    public ArrayList<String> getNewsContent() {
        return newsContent;
    }

    public void setMuseumName(String museumName) {
        this.museumName = museumName;
    }

    public void setEvaluation(String evaluation) {
        this.evaluation = evaluation;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public void setNewsId(int newsId) {
        this.newsId = newsId;
    }

    public void setNewsTitle(String newsTitle) {
        this.newsTitle = newsTitle;
    }

    public void setNewsContent(ArrayList<String> newsContent) {
        this.newsContent = newsContent;
    }
}
