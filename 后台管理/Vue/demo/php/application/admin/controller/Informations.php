<?php
// +----------------------------------------------------------------------
// | Description: 系统用户
// +----------------------------------------------------------------------
// | Author: linchuangbin <linchuangbin@honraytech.com>
// +----------------------------------------------------------------------
// use think\Controller;
namespace app\admin\controller;

class Informations extends Controller
{

    public function index()
    {   
        $InformationModel = model('Information');
        $param = $this->param;
        $keywords = !empty($param['keywords']) ? $param['keywords']: '';
        $page = !empty($param['page']) ? $param['page']: '';
        $limit = !empty($param['limit']) ? $param['limit']: '';    
        $data = $InformationModel->getDataList($keywords, $page, $limit);
        return resultArray(['data' => $data]);
    }

    public function read()
    {   
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->getDataById($param['id']);
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => $data]);
    }

    public function save()
    {
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->createData($param);
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => '添加成功']);
    }

    public function update()
    {
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->updateDataById($param, $param['id']);
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => '编辑成功']);
    }

    public function delete()
    {
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->delDataById($param['id']);       
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => '删除成功']);    
    }

    public function deletes()
    {
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->delDatas($param['ids']);  
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => '删除成功']); 
    }

    public function enables()
    {
        $InformationModel = model('Information');
        $param = $this->param;
        $data = $InformationModel->enableDatas($param['ids'], $param['status']);  
        if (!$data) {
            return resultArray(['error' => $InformationModel->getError()]);
        } 
        return resultArray(['data' => '操作成功']);         
    }

    /**
    @author wt
    **/

    public function getUserList(){
        $InformationModel=model('Information');
        $data = $InformationModel->getUserList();
        return $data;



    }
    
}
 