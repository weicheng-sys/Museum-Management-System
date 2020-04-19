package com.software.domain;
public class News {
	private int nid;
	private String title;
	private String content;
	private String nimg;
	private String ntime;
	private String publisher;
	
	public News() {
		// TODO Auto-generated constructor stub
	}

	public News(int nid, String title, String content, String nimg, String ntime, String publisher) {
		super();
		this.nid = nid;
		this.title = title;
		this.content = content;
		this.nimg = nimg;
		this.ntime = ntime;
		this.publisher = publisher;
	}

	@Override
	public String toString() {
		return "News [nid=" + nid + ", title=" + title + ", content=" + content + ", nimg=" + nimg + ", ntime=" + ntime
				+ ", publisher=" + publisher + "]";
	}

	public int getNid() {
		return nid;
	}

	public void setNid(int nid) {
		this.nid = nid;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getNimg() {
		return nimg;
	}

	public void setNimg(String nimg) {
		this.nimg = nimg;
	}

	public String getNtime() {
		return ntime;
	}

	public void setNtime(String ntime) {
		this.ntime = ntime;
	}

	public String getPublisher() {
		return publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}
	
	
}
