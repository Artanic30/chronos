<template>
  <el-form ref="EventForm" :model="EventForm" label-position="left">
    <el-form-item label="事件名称">
      <el-input v-model="EventForm.Name"></el-input>
    </el-form-item>
    <el-form-item label="开始时间">
      <el-date-picker type="datetime" v-model="EventForm.StartDatetime"></el-date-picker>
    </el-form-item>
    <el-form-item label="结束时间">
      <el-date-picker type="datetime" v-model="EventForm.EndDatetime"></el-date-picker>
    </el-form-item>
    <el-form-item label="地点">
      <el-autocomplete v-model="EventForm.Place" :fetch-suggestions="querySearchAsync" placeholder="请输入地点">
      </el-autocomplete>
    </el-form-item>
    <el-form-item label="事件内容">
      <el-input type="textarea" v-model="EventForm.Content"></el-input>
    </el-form-item>
    <el-form-item label="心情" v-if=" event_type === 'Past'">
      <!--TODO: emotion component-->
      <el-rate v-model="EventForm.Emotion"></el-rate>
    </el-form-item>
    <el-form-item label="">
      <el-button @click="EventSubmit()">提交</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    props: {
      event_type: {
        default: 'Past'
      },
      start_datetime: {},
      end_datetime: {}
    },
    data () {
      return {
        EventForm: {
          Name: '',
          Type: this.GetType,
          Content: '',
          StartDatetime: this.GetStartDatetime,
          EndDatetime: this.GetEndDatetime,
          Emotion: 0,
          Place: ''
        },
        PlaceChoices: [
          {'value': '三全鲜食（北新泾店）', 'address': '长宁区新渔路144号'},
          {'value': 'Hot honey 首尔炸鸡（仙霞路）', 'address': '上海市长宁区淞虹路661号'},
          {'value': '新旺角茶餐厅', 'address': '上海市普陀区真北路988号创邑金沙谷6号楼113'},
          {'value': '泷千家(天山西路店)', 'address': '天山西路438号'},
          {'value': '胖仙女纸杯蛋糕（上海凌空店）', 'address': '上海市长宁区金钟路968号1幢18号楼一层商铺18-101'},
          {'value': '贡茶', 'address': '上海市长宁区金钟路633号'},
          {'value': '豪大大香鸡排超级奶爸', 'address': '上海市嘉定区曹安公路曹安路1685号'},
          {'value': '茶芝兰（奶茶，手抓饼）', 'address': '上海市普陀区同普路1435号'},
          {'value': '十二泷町', 'address': '上海市北翟路1444弄81号B幢-107'},
          {'value': '星移浓缩咖啡', 'address': '上海市嘉定区新郁路817号'},
          {'value': '阿姨奶茶/豪大大', 'address': '嘉定区曹安路1611号'},
          {'value': '新麦甜四季甜品炸鸡', 'address': '嘉定区曹安公路2383弄55号'},
          {'value': 'Monica摩托主题咖啡店', 'address': '嘉定区江桥镇曹安公路2409号1F，2383弄62号1F'},
          {'value': '浮生若茶（凌空soho店）', 'address': '上海长宁区金钟路968号9号楼地下一层'},
          {'value': 'NONO JUICE  鲜榨果汁', 'address': '上海市长宁区天山西路119号'},
          {'value': 'CoCo都可(北新泾店）', 'address': '上海市长宁区仙霞西路'}
        ]
      }
    },
    methods: {
      EventSubmit () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Name: this.EventForm.Name,
            Type: this.EventForm.Type,
            Content: this.EventForm.Content,
            StartDatetime: this.EventForm.StartDatetime,
            EndDatetime: this.EventForm.EndDatetime,
            Emotion: this.EventForm.Emotion,
            Place: this.EventForm.Place,
            Token: this.GetToken
          })
        })
      },
      querySearchAsync (queryString, cb) {
        var PlaceChoices = []
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            place: this.place
          })
        }).then(function (response) {
          if (response.data.message === 'Success') {
            this.PlaceChoices = JSON.parse(response.data.data)
            clearTimeout(this.timeout)
            this.timeout = setTimeout(() => {
              cb(PlaceChoices)
            }, 3000 * Math.random())
          } else if (response.data.message === 'Error') {
            this.$notify.error({
              'title': '错误',
              'message': '获取地点数据失败'
            })
          }
        }.bind(this))
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetUserName () {
        return this.$store.state.UserName
      },
      GetToken () {
        return this.$store.state.Token
      },
      GetType () {
        return this.$props.event_type
      },
      GetStartDatetime () {
        return this.$props.start_datetime
      },
      GetEndDatetime () {
        return this.$props.end_datetime
      }
    }
  }
</script>
<style>
</style>
