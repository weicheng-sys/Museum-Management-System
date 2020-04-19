package com.software.domain;
public class Collection {
	private int mid;
	private String cname;
	private String cimg;
	private String years;
	private String explain;
	private String size;
	private String src;
	
	public Collection() {
		// TODO Auto-generated constructor stub
	}

	public Collection(int mid, String cname, String cimg, String years, String explain, String size, String src) {
		super();
		this.mid = mid;
		this.cname = cname;
		this.cimg = cimg;
		this.years = years;
		this.explain = explain;
		this.size = size;
		this.src = src;
	}

	@Override
	public String toString() {
		return "Collection [mid=" + mid + ", cname=" + cname + ", cimg=" + cimg + ", years=" + years + ", explain="
				+ explain + ", size=" + size + ", src=" + src + "]";
	}

	public int getMid() {
		return mid;
	}

	public void setMid(int mid) {
		this.mid = mid;
	}

	public String getCname() {
		return cname;
	}

	public void setCname(String cname) {
		this.cname = cname;
	}

	public String getCimg() {
		return cimg;
	}

	public void setCimg(String cimg) {
		this.cimg = cimg;
	}

	public String getYears() {
		return years;
	}

	public void setYears(String years) {
		this.years = years;
	}

	public String getExplain() {
		return explain;
	}

	public void setExplain(String explain) {
		this.explain = explain;
	}

	public String getSize() {
		return size;
	}

	public void setSize(String size) {
		this.size = size;
	}

	public String getSrc() {
		return src;
	}

	public void setSrc(String src) {
		this.src = src;
	}
	
	
}
